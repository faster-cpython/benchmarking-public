# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 172 ms: 1.12x faster                                                  |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                |
| html5lib       | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| tornado_http   | 86.7 ms                                                | 68.1 ms: 1.27x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 219 ms: 1.78x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 271 ms: 1.75x faster                                                  |
| async_tree_io           | 980 ms                                                 | 573 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 480 ms: 1.35x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.64x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.5 ms: 1.48x faster                                                 |
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.5 ms: 1.33x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 173 us: 1.62x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.47x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 36.1 ms: 1.29x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.40 ms: 1.27x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 52.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 70.6 ms: 1.02x faster                                                 |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| unpickle             | 8.80 us                                                | 9.28 us: 1.05x slower                                                 |
| pickle               | 6.97 us                                                | 7.50 us: 1.08x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.97 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.2 ms: 1.31x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 11.3 ms: 1.43x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.46 ms: 1.53x faster                                                 |
| django_template | 26.4 ms                                                | 21.6 ms: 1.22x faster                                                 |
| genshi_text     | 17.3 ms                                                | 15.9 ms: 1.09x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 35.2 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.0 us: 3.40x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.35 ms: 2.09x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.05x faster                                                 |
| logging_silent           | 117 ns                                                 | 62.6 ns: 1.87x faster                                                 |
| raytrace                 | 301 ms                                                 | 162 ms: 1.86x faster                                                  |
| deepcopy                 | 272 us                                                 | 151 us: 1.80x faster                                                  |
| async_tree_none          | 388 ms                                                 | 219 ms: 1.78x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 271 ms: 1.75x faster                                                  |
| async_tree_io            | 980 ms                                                 | 573 ms: 1.71x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.4 ms: 1.67x faster                                                 |
| richards_super           | 57.8 ms                                                | 35.5 ms: 1.63x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 173 us: 1.62x faster                                                  |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                                 |
| mako                     | 9.87 ms                                                | 6.46 ms: 1.53x faster                                                 |
| pylint                   | 277 ms                                                 | 183 ms: 1.51x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.51x faster                                                 |
| go                       | 151 ms                                                 | 100 ms: 1.51x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 827 us: 1.50x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.9 ms: 1.49x faster                                                 |
| float                    | 69.0 ms                                                | 46.5 ms: 1.48x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.01 us: 1.48x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| logging_format           | 4.83 us                                                | 3.31 us: 1.46x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 453 ms: 1.46x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.34 ms: 1.43x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.0 ms: 1.42x faster                                                 |
| generators               | 32.3 ms                                                | 23.3 ms: 1.39x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.2 ms: 1.38x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| pprint_safe_repr         | 641 ms                                                 | 467 ms: 1.37x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.37x faster                                                 |
| pyflate                  | 427 ms                                                 | 314 ms: 1.36x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 962 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 480 ms: 1.35x faster                                                  |
| regex_compile            | 95.3 ms                                                | 71.5 ms: 1.33x faster                                                 |
| pycparser                | 877 ms                                                 | 671 ms: 1.31x faster                                                  |
| thrift                   | 572 us                                                 | 441 us: 1.30x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 36.1 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| scimark_lu               | 103 ms                                                 | 80.5 ms: 1.28x faster                                                 |
| tornado_http             | 86.7 ms                                                | 68.1 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.40 ms: 1.27x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 74.0 ms: 1.25x faster                                                 |
| scimark_sor              | 128 ms                                                 | 103 ms: 1.24x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                                |
| fannkuch                 | 303 ms                                                 | 246 ms: 1.23x faster                                                  |
| django_template          | 26.4 ms                                                | 21.6 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 186 ms: 1.21x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.19x faster                                                 |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.93 ms: 1.17x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                |
| dask                     | 253 ms                                                 | 224 ms: 1.13x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.45 sec: 1.13x faster                                                |
| 2to3                     | 192 ms                                                 | 172 ms: 1.12x faster                                                  |
| sympy_expand             | 269 ms                                                 | 241 ms: 1.11x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.0 ms: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 475 us: 1.11x faster                                                  |
| genshi_text              | 17.3 ms                                                | 15.9 ms: 1.09x faster                                                 |
| nqueens                  | 63.8 ms                                                | 58.5 ms: 1.09x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.7 ms: 1.08x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 177 ms: 1.07x faster                                                  |
| pathlib                  | 24.5 ms                                                | 23.2 ms: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 52.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 70.6 ms: 1.02x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 35.2 ms: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.48 ms: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 906 us: 1.05x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.28 us: 1.05x slower                                                 |
| pickle                   | 6.97 us                                                | 7.50 us: 1.08x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.97 us: 1.09x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.3 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                  |
| python_startup           | 10.9 ms                                                | 14.2 ms: 1.31x slower                                                 |
| telco                    | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 49.2 ms: 1.31x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 11.3 ms: 1.43x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (13) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.41x