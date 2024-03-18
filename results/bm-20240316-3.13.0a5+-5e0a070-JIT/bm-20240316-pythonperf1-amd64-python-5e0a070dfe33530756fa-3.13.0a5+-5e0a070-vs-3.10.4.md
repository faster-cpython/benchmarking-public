# Results vs. 3.10.4

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                      |
| html5lib       | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                       |
| tornado_http   | 108 ms                                                      | 85.1 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 262 ms: 1.66x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 710 ms: 1.56x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 338 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 446 ms: 1.43x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.55x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.8 ms: 1.26x faster                                                       |
| nbody          | 71.3 ms                                                     | 58.2 ms: 1.23x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.6 ms: 1.27x faster                                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.53 ms: 1.66x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 178 us: 1.51x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.56 us: 1.06x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.7 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 17.4 us: 1.01x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| pickle               | 6.85 us                                                     | 7.15 us: 1.04x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.93 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.0 ms: 1.16x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 21.8 ms: 1.40x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.65 ms: 1.60x faster                                                       |
| django_template | 28.9 ms                                                     | 21.4 ms: 1.35x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 68.7 us: 4.89x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.03 ms: 2.06x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.1 ns: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.1 ms: 1.68x faster                                                       |
| pylint                   | 350 ms                                                      | 209 ms: 1.67x faster                                                        |
| async_tree_none          | 435 ms                                                      | 262 ms: 1.66x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.53 ms: 1.66x faster                                                       |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.65 ms: 1.60x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 710 ms: 1.56x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 338 ms: 1.56x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 781 us: 1.56x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.7 ms: 1.55x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.55x faster                                                        |
| raytrace                 | 273 ms                                                      | 179 ms: 1.52x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.9 ms: 1.52x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 178 us: 1.51x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 51.8 ms: 1.49x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1000 us: 1.48x faster                                                       |
| go                       | 139 ms                                                      | 95.2 ms: 1.46x faster                                                       |
| pyflate                  | 409 ms                                                      | 281 ms: 1.45x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 43.7 ms: 1.43x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 446 ms: 1.43x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.6 ms: 1.38x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.4 ms: 1.35x faster                                                       |
| pycparser                | 930 ms                                                      | 690 ms: 1.35x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.28 ms: 1.34x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.9 us: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                       |
| mypy2                    | 555 ms                                                      | 436 ms: 1.27x faster                                                        |
| tornado_http             | 108 ms                                                      | 85.1 ms: 1.27x faster                                                       |
| scimark_sor              | 106 ms                                                      | 83.5 ms: 1.27x faster                                                       |
| regex_compile            | 106 ms                                                      | 83.6 ms: 1.27x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 963 ms: 1.27x faster                                                        |
| float                    | 61.7 ms                                                     | 48.8 ms: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 473 ms: 1.25x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.71 sec: 1.24x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| nbody                    | 71.3 ms                                                     | 58.2 ms: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.6 ms: 1.22x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.24 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 71.9 ms: 1.19x faster                                                       |
| sympy_str                | 194 ms                                                      | 163 ms: 1.19x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.17x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.17x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.5 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 830 us: 1.15x faster                                                        |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| deepcopy                 | 255 us                                                      | 224 us: 1.14x faster                                                        |
| fannkuch                 | 256 ms                                                      | 225 ms: 1.14x faster                                                        |
| sympy_expand             | 314 ms                                                      | 279 ms: 1.13x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.7 ms: 1.12x faster                                                       |
| scimark_fft              | 187 ms                                                      | 169 ms: 1.11x faster                                                        |
| aiohttp                  | 995 us                                                      | 899 us: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.25 us: 1.08x faster                                                       |
| create_gc_cycles         | 800 us                                                      | 745 us: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.56 us: 1.06x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.86 us: 1.06x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.7 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.4 ms: 1.04x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 17.4 us: 1.01x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 76.8 ms: 1.01x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.15 us: 1.04x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.93 us: 1.07x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.51 ms: 1.07x slower                                                       |
| async_generators         | 222 ms                                                      | 239 ms: 1.08x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 70.2 ms: 1.13x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.0 ms: 1.16x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 46.9 ns: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 21.8 ms: 1.40x slower                                                       |
| thrift                   | 617 us                                                      | 8.84 ms: 14.31x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x


# Memory

- memory change: unknown