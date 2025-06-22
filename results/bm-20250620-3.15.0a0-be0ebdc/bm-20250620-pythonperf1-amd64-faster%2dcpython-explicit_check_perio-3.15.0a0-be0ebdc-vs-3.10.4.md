# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.277x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                                |
| nbody          | 71.3 ms                                                     | 62.5 ms: 1.14x faster                                                                |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.1 ms: 1.31x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                                |
| regex_dna      | 136 ms                                                      | 122 ms: 1.11x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                                |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.39 ms: 1.43x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.36x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 216 us: 1.25x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                                |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                                         |

Benchmark hidden because not significant (2): json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                                |
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                                |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.25x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.37x faster                                                                |
| mdp                      | 1.78 sec                                                    | 811 ms: 2.19x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                                |
| go                       | 139 ms                                                      | 76.2 ms: 1.82x faster                                                                |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.69x faster                                                                |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.67x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.4 us: 1.56x faster                                                                |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.56x faster                                                                |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.55x faster                                                                |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                                |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                                 |
| deepcopy                 | 255 us                                                      | 173 us: 1.48x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 58.6 ms: 1.46x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.3 ms: 1.46x faster                                                                |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 73.9 ms: 1.44x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.39 ms: 1.43x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.04 ms: 1.42x faster                                                                |
| float                    | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.36x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 47.5 ms: 1.32x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                                |
| regex_compile            | 106 ms                                                      | 81.1 ms: 1.31x faster                                                                |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 216 us: 1.25x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 62.6 ms: 1.23x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 41.4 ms: 1.22x faster                                                                |
| thrift                   | 617 us                                                      | 507 us: 1.22x faster                                                                 |
| sympy_sum                | 107 ms                                                      | 88.3 ms: 1.21x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                               |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                                |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 62.5 ms: 1.14x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                                |
| regex_dna                | 136 ms                                                      | 122 ms: 1.11x faster                                                                 |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.11x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.09x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                               |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                                |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 552 ms: 1.07x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 73.9 ms: 1.03x faster                                                                |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| fannkuch                 | 256 ms                                                      | 260 ms: 1.02x slower                                                                 |
| logging_simple           | 6.22 us                                                     | 6.36 us: 1.02x slower                                                                |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.52 ms: 1.15x slower                                                                |
| coverage                 | 39.0 ms                                                     | 48.2 ms: 1.24x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 323 ns: 3.41x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                                         |

Benchmark hidden because not significant (3): logging_format, json_loads, xml_etree_generate
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.277x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown