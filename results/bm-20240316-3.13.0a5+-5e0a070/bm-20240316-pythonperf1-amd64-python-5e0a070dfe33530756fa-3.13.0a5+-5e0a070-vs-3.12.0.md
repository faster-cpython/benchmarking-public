# Results vs. 3.12.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 209 ms: 1.04x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.82 ms: 1.03x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 83.8 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 260 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 444 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 336 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 719 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 469 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 268 ms: 1.07x faster                                                        |
| async_tree_io              | 731 ms                                                      | 702 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| nbody          | 71.9 ms                                                     | 73.4 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.3 ms: 1.13x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 18.1 ms: 1.27x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 176 us: 1.11x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                       |
| pickle               | 7.43 us                                                     | 7.05 us: 1.05x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.71 us: 1.01x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 93.7 ms: 1.01x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.91 us: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.61 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.23 ms: 1.14x faster                                                       |
| django_template | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 70.1 us: 1.36x faster                                                       |
| mypy2                      | 509 ms                                                      | 410 ms: 1.24x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.72 sec: 1.22x faster                                                      |
| raytrace                   | 192 ms                                                      | 163 ms: 1.18x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.23 ms: 1.14x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 77.3 ms: 1.13x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.4 ms: 1.12x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 43.3 ms: 1.12x faster                                                       |
| async_tree_none            | 291 ms                                                      | 260 ms: 1.12x faster                                                        |
| sympy_str                  | 175 ms                                                      | 157 ms: 1.11x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 176 us: 1.11x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 54.4 ns: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.1 ms: 1.11x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 82.8 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 444 ms: 1.10x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.97 ms: 1.09x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 336 ms: 1.09x faster                                                        |
| hexiom                     | 4.10 ms                                                     | 3.77 ms: 1.09x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| go                         | 91.6 ms                                                     | 84.4 ms: 1.08x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.9 us: 1.08x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                       |
| float                      | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 174 ms: 1.08x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 797 us: 1.08x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 62.3 ms: 1.07x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 64.4 ms: 1.07x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 58.5 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 719 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 469 ms: 1.07x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 752 us: 1.07x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 83.8 ms: 1.07x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.2 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 268 ms: 1.07x faster                                                        |
| deepcopy                   | 238 us                                                      | 224 us: 1.06x faster                                                        |
| logging_simple             | 6.28 us                                                     | 5.92 us: 1.06x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.06x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.36 us: 1.06x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 487 ms: 1.05x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 76.3 ms: 1.05x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.05 us: 1.05x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 462 ms: 1.05x faster                                                        |
| generators                 | 22.5 ms                                                     | 21.4 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 993 ms: 1.05x faster                                                        |
| sympy_expand               | 284 ms                                                      | 270 ms: 1.05x faster                                                        |
| django_template            | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 973 us: 1.05x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 71.3 ms: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.0 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.45 ms: 1.05x faster                                                       |
| async_tree_io              | 731 ms                                                      | 702 ms: 1.04x faster                                                        |
| 2to3                       | 218 ms                                                      | 209 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| pyflate                    | 295 ms                                                      | 284 ms: 1.04x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.4 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.82 ms: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                                        |
| create_gc_cycles           | 752 us                                                      | 730 us: 1.03x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 36.4 ns: 1.03x faster                                                       |
| scimark_fft                | 184 ms                                                      | 180 ms: 1.03x faster                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.49 ms: 1.02x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.01x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.71 us: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 93.7 ms: 1.01x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 79.6 ms: 1.01x slower                                                       |
| nbody                      | 71.9 ms                                                     | 73.4 ms: 1.02x slower                                                       |
| fannkuch                   | 247 ms                                                      | 252 ms: 1.02x slower                                                        |
| pickle_list                | 2.83 us                                                     | 2.91 us: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.61 us: 1.05x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.4 ms: 1.11x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.68 ms: 1.13x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 18.1 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (7): async_tree_memoization, aiohttp, pickle_dict, regex_effbot, regex_dna, pycparser, json
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x


# Memory

- memory change: unknown