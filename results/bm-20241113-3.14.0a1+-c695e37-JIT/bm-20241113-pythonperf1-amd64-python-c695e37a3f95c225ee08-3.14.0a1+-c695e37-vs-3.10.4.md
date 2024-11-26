# Results vs. 3.10.4

- fork: python
- ref: c695e37a3f95c225ee08
- machine: windows-amd64
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.207x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.92 sec                                                    | 1.89 sec: 1.01x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.08x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 262 ms: 2.01x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 553 ms: 2.01x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                       |
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.2 ms: 1.18x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.38 ms: 1.44x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.30x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.24x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                       |
| django_template | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 117 us: 2.86x faster                                                        |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.08x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 262 ms: 2.01x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 553 ms: 2.01x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 16.2 us: 1.78x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.36 ms: 1.77x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.6 ns: 1.73x faster                                                       |
| scimark_sor              | 106 ms                                                      | 64.1 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 54.2 ms: 1.58x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 39.6 ms: 1.58x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.9 ms: 1.55x faster                                                       |
| go                       | 139 ms                                                      | 91.0 ms: 1.53x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.4 ms: 1.49x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.38 ms: 1.44x faster                                                       |
| generators               | 32.4 ms                                                     | 22.8 ms: 1.42x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 55.4 ms: 1.39x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 899 us: 1.35x faster                                                        |
| nbody                    | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.4 ms: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 924 ms: 1.32x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 452 ms: 1.31x faster                                                        |
| pyflate                  | 409 ms                                                      | 313 ms: 1.31x faster                                                        |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.30x faster                                                        |
| pycparser                | 930 ms                                                      | 718 ms: 1.30x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.8 ms: 1.27x faster                                                       |
| pylint                   | 350 ms                                                      | 277 ms: 1.27x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.18 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.24x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.22 ms: 1.23x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                       |
| raytrace                 | 273 ms                                                      | 225 ms: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| richards                 | 42.4 ms                                                     | 35.2 ms: 1.21x faster                                                       |
| scimark_fft              | 187 ms                                                      | 155 ms: 1.21x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.2 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| thrift                   | 617 us                                                      | 527 us: 1.17x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 822 us: 1.16x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.19 ms: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.06x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                       |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                                        |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.05x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.9 ms: 1.04x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.56 us: 1.03x faster                                                       |
| sympy_str                | 194 ms                                                      | 190 ms: 1.03x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.10 us: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.89 sec: 1.01x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 65.7 ms: 1.01x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.9 ms: 1.01x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 15.6 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| sympy_expand             | 314 ms                                                      | 322 ms: 1.02x slower                                                        |
| sqlglot_normalize        | 205 ms                                                      | 210 ms: 1.02x slower                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 42.9 ms: 1.08x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.43 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                       |
| async_generators         | 222 ms                                                      | 267 ms: 1.21x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.8 ms: 1.23x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.91 ms: 1.36x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.7 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.72x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): 2to3
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.207x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown