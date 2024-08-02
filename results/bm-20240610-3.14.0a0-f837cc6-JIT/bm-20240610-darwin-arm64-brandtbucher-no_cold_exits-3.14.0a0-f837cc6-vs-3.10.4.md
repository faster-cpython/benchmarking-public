# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: darwin-arm64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 168 ms: 1.14x faster                                                 |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.16x faster                                               |
| html5lib       | 42.4 ms                                                | 30.7 ms: 1.38x faster                                                |
| tornado_http   | 86.7 ms                                                | 67.9 ms: 1.28x faster                                                |
| Geometric mean | (ref)                                                  | 1.23x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 214 ms: 1.81x faster                                                 |
| async_tree_memoization  | 474 ms                                                 | 263 ms: 1.80x faster                                                 |
| async_tree_io           | 980 ms                                                 | 571 ms: 1.72x faster                                                 |
| async_tree_cpu_io_mixed | 649 ms                                                 | 472 ms: 1.38x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.67x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                |
| float          | 69.0 ms                                                | 47.6 ms: 1.45x faster                                                |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.4 ms: 1.30x faster                                                |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                 |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 173 us: 1.63x faster                                                 |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.48x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.35x faster                                               |
| xml_etree_process    | 46.5 ms                                                | 35.9 ms: 1.30x faster                                                |
| json_dumps           | 8.11 ms                                                | 6.31 ms: 1.28x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 51.2 ms: 1.04x faster                                                |
| xml_etree_iterparse  | 72.1 ms                                                | 70.1 ms: 1.03x faster                                                |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                |
| unpickle             | 8.80 us                                                | 9.31 us: 1.06x slower                                                |
| pickle               | 6.97 us                                                | 7.45 us: 1.07x slower                                                |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                                |
| unpickle_list        | 2.69 us                                                | 3.07 us: 1.14x slower                                                |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.1 ms: 1.30x slower                                                |
| python_startup_no_site | 7.91 ms                                                | 11.6 ms: 1.46x slower                                                |
| Geometric mean         | (ref)                                                  | 1.38x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.36 ms: 1.55x faster                                                |
| django_template | 26.4 ms                                                | 21.4 ms: 1.24x faster                                                |
| genshi_text     | 17.3 ms                                                | 16.1 ms: 1.08x faster                                                |
| genshi_xml      | 33.8 ms                                                | 39.6 ms: 1.17x slower                                                |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.1 us: 3.43x faster                                                |
| deltablue                | 4.91 ms                                                | 2.46 ms: 2.00x faster                                                |
| logging_silent           | 117 ns                                                 | 62.3 ns: 1.88x faster                                                |
| raytrace                 | 301 ms                                                 | 165 ms: 1.83x faster                                                 |
| async_tree_none          | 388 ms                                                 | 214 ms: 1.81x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 263 ms: 1.80x faster                                                 |
| async_tree_io            | 980 ms                                                 | 571 ms: 1.72x faster                                                 |
| richards_super           | 57.8 ms                                                | 34.2 ms: 1.69x faster                                                |
| chaos                    | 65.8 ms                                                | 39.5 ms: 1.67x faster                                                |
| deepcopy_memo            | 34.7 us                                                | 21.2 us: 1.63x faster                                                |
| pickle_pure_python       | 281 us                                                 | 173 us: 1.63x faster                                                 |
| richards                 | 48.7 ms                                                | 30.4 ms: 1.60x faster                                                |
| asyncio_tcp              | 659 ms                                                 | 415 ms: 1.59x faster                                                 |
| mako                     | 9.87 ms                                                | 6.36 ms: 1.55x faster                                                |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 44.0 ms: 1.49x faster                                                |
| sqlglot_parse            | 1.24 ms                                                | 840 us: 1.48x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.48x faster                                                 |
| go                       | 151 ms                                                 | 103 ms: 1.47x faster                                                 |
| nbody                    | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                |
| float                    | 69.0 ms                                                | 47.6 ms: 1.45x faster                                                |
| logging_simple           | 4.45 us                                                | 3.09 us: 1.44x faster                                                |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                |
| logging_format           | 4.83 us                                                | 3.39 us: 1.43x faster                                                |
| spectral_norm            | 94.8 ms                                                | 67.2 ms: 1.41x faster                                                |
| hexiom                   | 6.19 ms                                                | 4.44 ms: 1.39x faster                                                |
| generators               | 32.3 ms                                                | 23.3 ms: 1.39x faster                                                |
| html5lib                 | 42.4 ms                                                | 30.7 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 472 ms: 1.38x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.36x faster                                                |
| crypto_pyaes             | 71.8 ms                                                | 52.8 ms: 1.36x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.35x faster                                               |
| pyflate                  | 427 ms                                                 | 320 ms: 1.34x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 483 ms: 1.33x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 986 ms: 1.32x faster                                                 |
| deepcopy                 | 272 us                                                 | 207 us: 1.31x faster                                                 |
| thrift                   | 572 us                                                 | 437 us: 1.31x faster                                                 |
| coroutines               | 20.7 ms                                                | 15.8 ms: 1.31x faster                                                |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.23 sec: 1.30x faster                                               |
| regex_compile            | 95.3 ms                                                | 73.4 ms: 1.30x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 35.9 ms: 1.30x faster                                                |
| pycparser                | 877 ms                                                 | 676 ms: 1.30x faster                                                 |
| scimark_lu               | 103 ms                                                 | 79.4 ms: 1.30x faster                                                |
| json_dumps               | 8.11 ms                                                | 6.31 ms: 1.28x faster                                                |
| tornado_http             | 86.7 ms                                                | 67.9 ms: 1.28x faster                                                |
| sympy_sum                | 92.2 ms                                                | 72.4 ms: 1.27x faster                                                |
| scimark_sor              | 128 ms                                                 | 101 ms: 1.27x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.83 us: 1.27x faster                                                |
| django_template          | 26.4 ms                                                | 21.4 ms: 1.24x faster                                                |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.22x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.21x faster                                                |
| fannkuch                 | 303 ms                                                 | 251 ms: 1.20x faster                                                 |
| sympy_str                | 165 ms                                                 | 138 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.92 ms: 1.17x faster                                                |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.16x faster                                               |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                 |
| 2to3                     | 192 ms                                                 | 168 ms: 1.14x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                               |
| sympy_expand             | 269 ms                                                 | 237 ms: 1.13x faster                                                 |
| pathlib                  | 24.5 ms                                                | 21.6 ms: 1.13x faster                                                |
| nqueens                  | 63.8 ms                                                | 57.1 ms: 1.12x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 33.2 ms: 1.11x faster                                                |
| bench_thread_pool        | 527 us                                                 | 481 us: 1.10x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.1 ms: 1.08x faster                                                |
| meteor_contest           | 77.7 ms                                                | 73.5 ms: 1.06x faster                                                |
| xml_etree_parse          | 108 ms                                                 | 102 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                |
| xml_etree_generate       | 53.5 ms                                                | 51.2 ms: 1.04x faster                                                |
| xml_etree_iterparse      | 72.1 ms                                                | 70.1 ms: 1.03x faster                                                |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                |
| create_gc_cycles         | 860 us                                                 | 895 us: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                |
| unpickle                 | 8.80 us                                                | 9.31 us: 1.06x slower                                                |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                |
| pickle                   | 6.97 us                                                | 7.45 us: 1.07x slower                                                |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                                |
| coverage                 | 41.5 ms                                                | 45.9 ms: 1.11x slower                                                |
| unpickle_list            | 2.69 us                                                | 3.07 us: 1.14x slower                                                |
| genshi_xml               | 33.8 ms                                                | 39.6 ms: 1.17x slower                                                |
| async_generators         | 231 ms                                                 | 287 ms: 1.24x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 48.0 ms: 1.28x slower                                                |
| python_startup           | 10.9 ms                                                | 14.1 ms: 1.30x slower                                                |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                |
| python_startup_no_site   | 7.91 ms                                                | 11.6 ms: 1.46x slower                                                |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.12x