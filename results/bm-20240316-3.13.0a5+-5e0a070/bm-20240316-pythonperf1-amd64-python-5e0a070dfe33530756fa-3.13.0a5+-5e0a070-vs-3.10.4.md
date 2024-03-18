# Results vs. 3.10.4

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 209 ms: 1.17x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.82 ms: 1.20x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                       |
| tornado_http   | 108 ms                                                      | 83.8 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 260 ms: 1.67x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 702 ms: 1.58x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 337 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 444 ms: 1.44x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.56x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| nbody          | 71.3 ms                                                     | 73.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.3 ms: 1.37x faster                                                       |
| regex_dna      | 136 ms                                                      | 127 ms: 1.08x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 176 us: 1.53x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.61 us: 1.06x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 93.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.02x faster                                                       |
| pickle               | 6.85 us                                                     | 7.05 us: 1.03x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.91 us: 1.06x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.23 ms: 1.45x faster                                                       |
| django_template | 28.9 ms                                                     | 21.8 ms: 1.32x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 70.1 us: 4.79x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.97 ms: 2.12x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.4 ns: 1.74x faster                                                       |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                        |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                       |
| raytrace                 | 273 ms                                                      | 163 ms: 1.67x faster                                                        |
| async_tree_none          | 435 ms                                                      | 260 ms: 1.67x faster                                                        |
| go                       | 139 ms                                                      | 84.4 ms: 1.65x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 752 us: 1.62x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.58x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 462 ms: 1.58x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 702 ms: 1.58x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 337 ms: 1.56x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 55.2 ms: 1.55x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 176 us: 1.53x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 3.77 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 973 us: 1.52x faster                                                        |
| generators               | 32.4 ms                                                     | 21.4 ms: 1.51x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.23 ms: 1.45x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 43.3 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 444 ms: 1.44x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.42x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.3 ms: 1.37x faster                                                       |
| mypy2                    | 555 ms                                                      | 410 ms: 1.36x faster                                                        |
| scimark_sor              | 106 ms                                                      | 79.6 ms: 1.33x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.8 ms: 1.32x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.9 us: 1.32x faster                                                       |
| pycparser                | 930 ms                                                      | 708 ms: 1.31x faster                                                        |
| tornado_http             | 108 ms                                                      | 83.8 ms: 1.29x faster                                                       |
| sympy_sum                | 107 ms                                                      | 82.8 ms: 1.29x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 39.4 ms: 1.28x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.25x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.3 ms: 1.24x faster                                                       |
| sympy_str                | 194 ms                                                      | 157 ms: 1.24x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 993 ms: 1.23x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.72 sec: 1.22x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 487 ms: 1.22x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 33.0 ms: 1.21x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 797 us: 1.20x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.82 ms: 1.20x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 174 ms: 1.18x faster                                                        |
| 2to3                     | 246 ms                                                      | 209 ms: 1.17x faster                                                        |
| float                    | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| sympy_expand             | 314 ms                                                      | 270 ms: 1.16x faster                                                        |
| deepcopy                 | 255 us                                                      | 224 us: 1.14x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 58.5 ms: 1.14x faster                                                       |
| aiohttp                  | 995 us                                                      | 882 us: 1.13x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.13x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.45 ms: 1.11x faster                                                       |
| create_gc_cycles         | 800 us                                                      | 730 us: 1.10x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 36.4 ns: 1.09x faster                                                       |
| regex_dna                | 136 ms                                                      | 127 ms: 1.08x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 71.3 ms: 1.06x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.36 us: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.61 us: 1.06x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.92 us: 1.05x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                       |
| scimark_fft              | 187 ms                                                      | 180 ms: 1.04x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 93.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| fannkuch                 | 256 ms                                                      | 252 ms: 1.01x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 76.3 ms: 1.01x slower                                                       |
| nbody                    | 71.3 ms                                                     | 73.4 ms: 1.03x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.05 us: 1.03x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 64.4 ms: 1.04x slower                                                       |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.91 us: 1.06x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.49 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.4 ms: 1.16x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.68 ms: 1.19x slower                                                       |
| thrift                   | 617 us                                                      | 8.03 ms: 13.00x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (3): python_startup, unpickle_list, json
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x


# Memory

- memory change: unknown