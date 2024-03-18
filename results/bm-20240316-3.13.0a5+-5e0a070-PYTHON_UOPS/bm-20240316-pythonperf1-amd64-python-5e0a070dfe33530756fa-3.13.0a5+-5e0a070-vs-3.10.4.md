# Results vs. 3.10.4

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.92 ms: 1.18x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| tornado_http   | 108 ms                                                      | 86.4 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 270 ms: 1.61x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 723 ms: 1.53x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 348 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 454 ms: 1.40x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.51x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.7 ms: 1.09x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| nbody          | 71.3 ms                                                     | 74.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| regex_compile  | 106 ms                                                      | 96.7 ms: 1.10x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.76 ms: 1.59x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 183 us: 1.47x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 38.2 ms: 1.16x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.31 us: 1.09x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.8 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| pickle               | 6.85 us                                                     | 7.19 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.2 us: 1.06x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.24 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.3 ms: 1.01x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                       |
| django_template | 28.9 ms                                                     | 22.4 ms: 1.29x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 73.1 us: 4.60x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.9 ns: 1.72x faster                                                       |
| pylint                   | 350 ms                                                      | 213 ms: 1.64x faster                                                        |
| async_tree_none          | 435 ms                                                      | 270 ms: 1.61x faster                                                        |
| richards_super           | 52.2 ms                                                     | 32.5 ms: 1.61x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.76 ms: 1.59x faster                                                       |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.56x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 723 ms: 1.53x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 480 ms: 1.53x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 348 ms: 1.51x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 819 us: 1.48x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.7 ms: 1.48x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 183 us: 1.47x faster                                                        |
| raytrace                 | 273 ms                                                      | 189 ms: 1.45x faster                                                        |
| chaos                    | 61.7 ms                                                     | 43.6 ms: 1.42x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 454 ms: 1.40x faster                                                        |
| go                       | 139 ms                                                      | 102 ms: 1.36x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.6 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| django_template          | 28.9 ms                                                     | 22.4 ms: 1.29x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.8 us: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 725 ms: 1.28x faster                                                        |
| tornado_http             | 108 ms                                                      | 86.4 ms: 1.25x faster                                                       |
| mypy2                    | 555 ms                                                      | 443 ms: 1.25x faster                                                        |
| pyflate                  | 409 ms                                                      | 327 ms: 1.25x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.71 sec: 1.23x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                       |
| scimark_sor              | 106 ms                                                      | 89.1 ms: 1.19x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 24.2 us: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.88 ms: 1.18x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.92 ms: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 91.7 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 38.2 ms: 1.16x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.4 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.3 ms: 1.14x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 523 ms: 1.13x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 76.1 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| regex_compile            | 106 ms                                                      | 96.7 ms: 1.10x faster                                                       |
| aiohttp                  | 995 us                                                      | 908 us: 1.10x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.31 us: 1.09x faster                                                       |
| deepcopy                 | 255 us                                                      | 234 us: 1.09x faster                                                        |
| float                    | 61.7 ms                                                     | 56.7 ms: 1.09x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 189 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                       |
| create_gc_cycles         | 800 us                                                      | 744 us: 1.07x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 73.0 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.8 ms: 1.05x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.04x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.55 us: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.12 us: 1.02x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.3 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.0 ms: 1.01x faster                                                       |
| fannkuch                 | 256 ms                                                      | 260 ms: 1.02x slower                                                        |
| nqueens                  | 66.6 ms                                                     | 68.1 ms: 1.02x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 77.8 ms: 1.03x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 40.9 ns: 1.03x slower                                                       |
| nbody                    | 71.3 ms                                                     | 74.4 ms: 1.04x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.19 us: 1.05x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 65.7 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.2 us: 1.06x slower                                                       |
| async_generators         | 222 ms                                                      | 237 ms: 1.07x slower                                                        |
| scimark_fft              | 187 ms                                                      | 201 ms: 1.07x slower                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.52 ms: 1.07x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.99 ms: 1.10x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.24 us: 1.18x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.76 ms: 1.21x slower                                                       |
| thrift                   | 617 us                                                      | 9.24 ms: 14.97x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, unpickle_list, json
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240316-3.13.0a5+-5e0a070-PYTHON_UOPS/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x


# Memory

- memory change: unknown