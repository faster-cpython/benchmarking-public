# Results vs. 3.10.4

- fork: python
- ref: ae4d27eba7c746463c62
- machine: windows-amd64
- commit hash: ae4d27e
- commit date: 2025-07-24
- overall geometric mean: 1.298x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 211 ms: 2.50x faster                                                       |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.45x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 338 ms: 1.89x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.39x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| nbody          | 71.3 ms                                                     | 55.7 ms: 1.28x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.4 ms: 1.30x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.13 sec: 1.48x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.39 ms: 1.43x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.29x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.0 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.48 ms: 1.65x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.3 ms: 1.22x faster                                                      |
| django_template | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.25x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 211 ms: 2.50x faster                                                       |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.45x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.9 ms: 2.30x faster                                                      |
| mdp                      | 1.78 sec                                                    | 815 ms: 2.18x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 338 ms: 1.89x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| go                       | 139 ms                                                      | 79.0 ms: 1.76x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                       |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.2 ms: 1.68x faster                                                      |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.48 ms: 1.65x faster                                                      |
| pyflate                  | 409 ms                                                      | 255 ms: 1.60x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.9 ms: 1.52x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.2 us: 1.50x faster                                                      |
| raytrace                 | 273 ms                                                      | 184 ms: 1.49x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.13 sec: 1.48x faster                                                     |
| chaos                    | 61.7 ms                                                     | 42.1 ms: 1.47x faster                                                      |
| deepcopy                 | 255 us                                                      | 176 us: 1.45x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.39 ms: 1.43x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.41x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.8 ms: 1.41x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 896 ms: 1.36x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                                      |
| float                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.28 ms: 1.34x faster                                                      |
| scimark_sor              | 106 ms                                                      | 79.4 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 698 ms: 1.33x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 446 ms: 1.33x faster                                                       |
| regex_compile            | 106 ms                                                      | 81.4 ms: 1.30x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.29x faster                                                       |
| nbody                    | 71.3 ms                                                     | 55.7 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 495 us: 1.25x faster                                                       |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.3 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.0 ms: 1.22x faster                                                      |
| fannkuch                 | 256 ms                                                      | 213 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.20x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 65.5 ms: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                      |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.4 ms: 1.06x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 298 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.40 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.0 ms: 1.03x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.22 ms: 1.07x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.54x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.29x faster                                                               |

Benchmark hidden because not significant (1): logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250724-3.15.0a0-ae4d27e-JIT/bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.298x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown