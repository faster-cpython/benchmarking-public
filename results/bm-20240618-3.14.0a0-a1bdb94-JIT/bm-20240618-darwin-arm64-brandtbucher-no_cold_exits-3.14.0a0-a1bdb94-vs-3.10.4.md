# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: darwin-arm64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.13x faster                                                 |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                               |
| html5lib       | 42.4 ms                                                | 30.7 ms: 1.38x faster                                                |
| tornado_http   | 86.7 ms                                                | 67.3 ms: 1.29x faster                                                |
| Geometric mean | (ref)                                                  | 1.23x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 217 ms: 1.79x faster                                                 |
| async_tree_memoization  | 474 ms                                                 | 268 ms: 1.77x faster                                                 |
| async_tree_io           | 980 ms                                                 | 580 ms: 1.69x faster                                                 |
| async_tree_cpu_io_mixed | 649 ms                                                 | 476 ms: 1.36x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.64x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.4 ms: 1.49x faster                                                |
| nbody          | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                |
| pidigits       | 282 ms                                                 | 286 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.1 ms: 1.32x faster                                                |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                 |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 176 us: 1.60x faster                                                 |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.47x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.27 sec: 1.35x faster                                               |
| json_dumps           | 8.11 ms                                                | 6.26 ms: 1.29x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 36.1 ms: 1.29x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 52.2 ms: 1.03x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 71.3 ms: 1.01x faster                                                |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                |
| unpickle             | 8.80 us                                                | 9.32 us: 1.06x slower                                                |
| pickle               | 6.97 us                                                | 7.49 us: 1.07x slower                                                |
| unpickle_list        | 2.69 us                                                | 2.93 us: 1.09x slower                                                |
| pickle_dict          | 17.0 us                                                | 18.6 us: 1.09x slower                                                |
| pickle_list          | 2.74 us                                                | 3.02 us: 1.10x slower                                                |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                |
| python_startup_no_site | 7.91 ms                                                | 12.3 ms: 1.56x slower                                                |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.46 ms: 1.53x faster                                                |
| django_template | 26.4 ms                                                | 21.9 ms: 1.21x faster                                                |
| genshi_text     | 17.3 ms                                                | 15.9 ms: 1.09x faster                                                |
| genshi_xml      | 33.8 ms                                                | 40.3 ms: 1.19x slower                                                |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.1 us: 3.43x faster                                                |
| deltablue                | 4.91 ms                                                | 2.36 ms: 2.08x faster                                                |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.06x faster                                                |
| logging_silent           | 117 ns                                                 | 62.5 ns: 1.87x faster                                                |
| raytrace                 | 301 ms                                                 | 162 ms: 1.86x faster                                                 |
| async_tree_none          | 388 ms                                                 | 217 ms: 1.79x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 268 ms: 1.77x faster                                                 |
| deepcopy                 | 272 us                                                 | 155 us: 1.75x faster                                                 |
| async_tree_io            | 980 ms                                                 | 580 ms: 1.69x faster                                                 |
| chaos                    | 65.8 ms                                                | 39.0 ms: 1.69x faster                                                |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.68x faster                                                |
| richards                 | 48.7 ms                                                | 30.4 ms: 1.60x faster                                                |
| pickle_pure_python       | 281 us                                                 | 176 us: 1.60x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 416 ms: 1.58x faster                                                 |
| mako                     | 9.87 ms                                                | 6.46 ms: 1.53x faster                                                |
| pylint                   | 277 ms                                                 | 183 ms: 1.51x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.55 us: 1.51x faster                                                |
| scimark_monte_carlo      | 65.6 ms                                                | 43.6 ms: 1.51x faster                                                |
| sqlglot_parse            | 1.24 ms                                                | 827 us: 1.50x faster                                                 |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                 |
| float                    | 69.0 ms                                                | 46.4 ms: 1.49x faster                                                |
| logging_simple           | 4.45 us                                                | 3.01 us: 1.48x faster                                                |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.47x faster                                                 |
| logging_format           | 4.83 us                                                | 3.30 us: 1.46x faster                                                |
| nbody                    | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                |
| sqlglot_transpile        | 1.44 ms                                                | 994 us: 1.45x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.3 ms: 1.41x faster                                                |
| generators               | 32.3 ms                                                | 23.2 ms: 1.40x faster                                                |
| crypto_pyaes             | 71.8 ms                                                | 51.5 ms: 1.39x faster                                                |
| hexiom                   | 6.19 ms                                                | 4.44 ms: 1.39x faster                                                |
| html5lib                 | 42.4 ms                                                | 30.7 ms: 1.38x faster                                                |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.37x faster                                                |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 476 ms: 1.36x faster                                                 |
| pyflate                  | 427 ms                                                 | 316 ms: 1.35x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 475 ms: 1.35x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.27 sec: 1.35x faster                                               |
| pprint_pformat           | 1.30 sec                                               | 976 ms: 1.34x faster                                                 |
| regex_compile            | 95.3 ms                                                | 72.1 ms: 1.32x faster                                                |
| thrift                   | 572 us                                                 | 438 us: 1.30x faster                                                 |
| pycparser                | 877 ms                                                 | 672 ms: 1.30x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.26 ms: 1.29x faster                                                |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                                |
| tornado_http             | 86.7 ms                                                | 67.3 ms: 1.29x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 36.1 ms: 1.29x faster                                                |
| scimark_lu               | 103 ms                                                 | 80.8 ms: 1.27x faster                                                |
| scimark_sor              | 128 ms                                                 | 102 ms: 1.26x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 73.4 ms: 1.26x faster                                                |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                               |
| fannkuch                 | 303 ms                                                 | 244 ms: 1.24x faster                                                 |
| django_template          | 26.4 ms                                                | 21.9 ms: 1.21x faster                                                |
| scimark_fft              | 224 ms                                                 | 187 ms: 1.20x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.20x faster                                                |
| sympy_str                | 165 ms                                                 | 139 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.92 ms: 1.17x faster                                                |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                               |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.14x faster                                               |
| 2to3                     | 192 ms                                                 | 170 ms: 1.13x faster                                                 |
| sympy_expand             | 269 ms                                                 | 239 ms: 1.13x faster                                                 |
| dask                     | 253 ms                                                 | 225 ms: 1.12x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 472 us: 1.12x faster                                                 |
| nqueens                  | 63.8 ms                                                | 57.3 ms: 1.11x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 33.1 ms: 1.11x faster                                                |
| genshi_text              | 17.3 ms                                                | 15.9 ms: 1.09x faster                                                |
| meteor_contest           | 77.7 ms                                                | 72.1 ms: 1.08x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 177 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                |
| xml_etree_generate       | 53.5 ms                                                | 52.2 ms: 1.03x faster                                                |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 71.3 ms: 1.01x faster                                                |
| pidigits                 | 282 ms                                                 | 286 ms: 1.01x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                |
| create_gc_cycles         | 860 us                                                 | 894 us: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                |
| unpickle                 | 8.80 us                                                | 9.32 us: 1.06x slower                                                |
| pickle                   | 6.97 us                                                | 7.49 us: 1.07x slower                                                |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                                |
| unpickle_list            | 2.69 us                                                | 2.93 us: 1.09x slower                                                |
| pickle_dict              | 17.0 us                                                | 18.6 us: 1.09x slower                                                |
| pickle_list              | 2.74 us                                                | 3.02 us: 1.10x slower                                                |
| coverage                 | 41.5 ms                                                | 46.3 ms: 1.12x slower                                                |
| genshi_xml               | 33.8 ms                                                | 40.3 ms: 1.19x slower                                                |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 48.7 ms: 1.30x slower                                                |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.31x slower                                                |
| python_startup           | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                |
| python_startup_no_site   | 7.91 ms                                                | 12.3 ms: 1.56x slower                                                |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (13) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.30x