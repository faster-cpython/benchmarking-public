# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.243x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                               |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                                |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 424 ms: 2.61x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 188 ms: 2.32x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 228 ms: 2.31x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 345 ms: 1.85x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.26x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                                |
| nbody          | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                                |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.1 ms: 1.26x faster                                                                |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 142 us: 1.29x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 222 us: 1.21x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 40.1 ms: 1.11x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                                |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 37.5 ms: 1.10x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.14x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 424 ms: 2.61x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.39x faster                                                                |
| async_tree_none          | 435 ms                                                      | 188 ms: 2.32x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 228 ms: 2.31x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 835 ms: 2.13x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 345 ms: 1.85x faster                                                                 |
| go                       | 139 ms                                                      | 79.3 ms: 1.75x faster                                                                |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 32.6 ms: 1.60x faster                                                                |
| generators               | 32.4 ms                                                     | 20.5 ms: 1.58x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                                |
| chaos                    | 61.7 ms                                                     | 41.0 ms: 1.50x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.49x faster                                                                |
| richards                 | 42.4 ms                                                     | 28.5 ms: 1.49x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                                |
| raytrace                 | 273 ms                                                      | 189 ms: 1.45x faster                                                                 |
| deepcopy                 | 255 us                                                      | 178 us: 1.43x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 60.1 ms: 1.43x faster                                                                |
| scimark_sor              | 106 ms                                                      | 75.2 ms: 1.41x faster                                                                |
| pyflate                  | 409 ms                                                      | 295 ms: 1.39x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.5 ms: 1.38x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.25 ms: 1.35x faster                                                                |
| float                    | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 142 us: 1.29x faster                                                                 |
| regex_compile            | 106 ms                                                      | 84.1 ms: 1.26x faster                                                                |
| pycparser                | 930 ms                                                      | 739 ms: 1.26x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 49.8 ms: 1.26x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                                |
| thrift                   | 617 us                                                      | 495 us: 1.25x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 62.1 ms: 1.24x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 222 us: 1.21x faster                                                                 |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                               |
| sympy_integrate          | 15.3 ms                                                     | 12.9 ms: 1.19x faster                                                                |
| sympy_sum                | 107 ms                                                      | 90.8 ms: 1.18x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                                |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                                |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 40.1 ms: 1.11x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                                |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 37.5 ms: 1.10x faster                                                                |
| nbody                    | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                                |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 566 ms: 1.05x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                                |
| sympy_expand             | 314 ms                                                      | 302 ms: 1.04x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.17 sec: 1.04x faster                                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 64.7 ms: 1.03x faster                                                                |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| meteor_contest           | 75.9 ms                                                     | 74.9 ms: 1.01x faster                                                                |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.01x faster                                                                 |
| fannkuch                 | 256 ms                                                      | 259 ms: 1.01x slower                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                                |
| logging_format           | 6.76 us                                                     | 7.14 us: 1.06x slower                                                                |
| async_generators         | 222 ms                                                      | 235 ms: 1.06x slower                                                                 |
| logging_simple           | 6.22 us                                                     | 6.62 us: 1.06x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                                |
| coverage                 | 39.0 ms                                                     | 49.7 ms: 1.27x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 323 ns: 3.41x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                         |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.243x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown