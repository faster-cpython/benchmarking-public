# Results vs. base

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                 | 285 ms: 1.01x slower                                               |
| docutils       | 2.77 sec                                                               | 2.79 sec: 1.01x slower                                             |
| html5lib       | 67.7 ms                                                                | 66.0 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none_tg | 459 ms                                                                 | 456 ms: 1.01x faster                                               |
| async_tree_io_tg   | 1.23 sec                                                               | 1.24 sec: 1.00x slower                                             |
| async_tree_io      | 1.21 sec                                                               | 1.22 sec: 1.01x slower                                             |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 190 ms: 1.00x faster                                               |
| float          | 80.1 ms                                                                | 81.5 ms: 1.02x slower                                              |
| nbody          | 94.4 ms                                                                | 97.9 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                 | 224 ms: 1.02x faster                                               |
| regex_effbot   | 3.76 ms                                                                | 3.92 ms: 1.04x slower                                              |
| regex_compile  | 144 ms                                                                 | 155 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_list        | 5.12 us                                                                | 5.09 us: 1.01x faster                                              |
| json_loads           | 27.9 us                                                                | 28.1 us: 1.01x slower                                              |
| pickle_pure_python   | 298 us                                                                 | 300 us: 1.01x slower                                               |
| xml_etree_generate   | 87.7 ms                                                                | 88.4 ms: 1.01x slower                                              |
| xml_etree_iterparse  | 107 ms                                                                 | 109 ms: 1.02x slower                                               |
| pickle               | 11.5 us                                                                | 11.8 us: 1.03x slower                                              |
| unpickle_pure_python | 238 us                                                                 | 246 us: 1.03x slower                                               |
| tomli_loads          | 2.09 sec                                                               | 2.17 sec: 1.04x slower                                             |
| pickle_list          | 4.96 us                                                                | 5.19 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, json_dumps, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 11.2 ms                                                                | 10.1 ms: 1.11x faster                                              |
| python_startup         | 12.6 ms                                                                | 11.5 ms: 1.10x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.10x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 34.3 ms                                                                | 34.6 ms: 1.01x slower                                              |
| genshi_xml      | 55.0 ms                                                                | 55.9 ms: 1.02x slower                                              |
| genshi_text     | 24.1 ms                                                                | 24.6 ms: 1.02x slower                                              |
| mako            | 10.9 ms                                                                | 11.4 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site   | 11.2 ms                                                                | 10.1 ms: 1.11x faster                                              |
| bench_mp_pool            | 26.4 ms                                                                | 24.0 ms: 1.10x faster                                              |
| python_startup           | 12.6 ms                                                                | 11.5 ms: 1.10x faster                                              |
| logging_silent           | 104 ns                                                                 | 100 ns: 1.03x faster                                               |
| html5lib                 | 67.7 ms                                                                | 66.0 ms: 1.02x faster                                              |
| pycparser                | 1.26 sec                                                               | 1.23 sec: 1.02x faster                                             |
| regex_dna                | 228 ms                                                                 | 224 ms: 1.02x faster                                               |
| mdp                      | 2.82 sec                                                               | 2.77 sec: 1.02x faster                                             |
| coroutines               | 23.3 ms                                                                | 23.0 ms: 1.01x faster                                              |
| typing_runtime_protocols | 111 us                                                                 | 109 us: 1.01x faster                                               |
| create_gc_cycles         | 1.52 ms                                                                | 1.51 ms: 1.01x faster                                              |
| async_tree_none_tg       | 459 ms                                                                 | 456 ms: 1.01x faster                                               |
| async_generators         | 472 ms                                                                 | 469 ms: 1.01x faster                                               |
| deepcopy_memo            | 39.1 us                                                                | 38.9 us: 1.01x faster                                              |
| unpickle_list            | 5.12 us                                                                | 5.09 us: 1.01x faster                                              |
| pidigits                 | 190 ms                                                                 | 190 ms: 1.00x faster                                               |
| asyncio_tcp_ssl          | 1.85 sec                                                               | 1.85 sec: 1.00x faster                                             |
| deepcopy                 | 350 us                                                                 | 351 us: 1.00x slower                                               |
| async_tree_io_tg         | 1.23 sec                                                               | 1.24 sec: 1.00x slower                                             |
| sympy_integrate          | 21.3 ms                                                                | 21.4 ms: 1.01x slower                                              |
| deepcopy_reduce          | 3.06 us                                                                | 3.08 us: 1.01x slower                                              |
| json_loads               | 27.9 us                                                                | 28.1 us: 1.01x slower                                              |
| generators               | 29.6 ms                                                                | 29.8 ms: 1.01x slower                                              |
| pickle_pure_python       | 298 us                                                                 | 300 us: 1.01x slower                                               |
| docutils                 | 2.77 sec                                                               | 2.79 sec: 1.01x slower                                             |
| scimark_sor              | 130 ms                                                                 | 130 ms: 1.01x slower                                               |
| xml_etree_generate       | 87.7 ms                                                                | 88.4 ms: 1.01x slower                                              |
| django_template          | 34.3 ms                                                                | 34.6 ms: 1.01x slower                                              |
| 2to3                     | 282 ms                                                                 | 285 ms: 1.01x slower                                               |
| async_tree_io            | 1.21 sec                                                               | 1.22 sec: 1.01x slower                                             |
| sympy_str                | 287 ms                                                                 | 290 ms: 1.01x slower                                               |
| sympy_sum                | 161 ms                                                                 | 163 ms: 1.01x slower                                               |
| thrift                   | 793 us                                                                 | 801 us: 1.01x slower                                               |
| deltablue                | 3.44 ms                                                                | 3.48 ms: 1.01x slower                                              |
| sqlglot_transpile        | 1.66 ms                                                                | 1.68 ms: 1.01x slower                                              |
| go                       | 158 ms                                                                 | 159 ms: 1.01x slower                                               |
| coverage                 | 97.7 ms                                                                | 98.8 ms: 1.01x slower                                              |
| sympy_expand             | 486 ms                                                                 | 492 ms: 1.01x slower                                               |
| dulwich_log              | 70.8 ms                                                                | 71.8 ms: 1.01x slower                                              |
| telco                    | 8.41 ms                                                                | 8.55 ms: 1.02x slower                                              |
| xml_etree_iterparse      | 107 ms                                                                 | 109 ms: 1.02x slower                                               |
| float                    | 80.1 ms                                                                | 81.5 ms: 1.02x slower                                              |
| sqlglot_optimize         | 56.6 ms                                                                | 57.6 ms: 1.02x slower                                              |
| richards_super           | 52.4 ms                                                                | 53.3 ms: 1.02x slower                                              |
| genshi_xml               | 55.0 ms                                                                | 55.9 ms: 1.02x slower                                              |
| meteor_contest           | 110 ms                                                                 | 112 ms: 1.02x slower                                               |
| raytrace                 | 297 ms                                                                 | 303 ms: 1.02x slower                                               |
| sqlite_synth             | 2.83 us                                                                | 2.89 us: 1.02x slower                                              |
| scimark_lu               | 131 ms                                                                 | 133 ms: 1.02x slower                                               |
| json                     | 5.20 ms                                                                | 5.32 ms: 1.02x slower                                              |
| genshi_text              | 24.1 ms                                                                | 24.6 ms: 1.02x slower                                              |
| pickle                   | 11.5 us                                                                | 11.8 us: 1.03x slower                                              |
| richards                 | 46.1 ms                                                                | 47.5 ms: 1.03x slower                                              |
| nqueens                  | 90.3 ms                                                                | 93.2 ms: 1.03x slower                                              |
| crypto_pyaes             | 75.5 ms                                                                | 77.9 ms: 1.03x slower                                              |
| unpickle_pure_python     | 238 us                                                                 | 246 us: 1.03x slower                                               |
| nbody                    | 94.4 ms                                                                | 97.9 ms: 1.04x slower                                              |
| chaos                    | 64.5 ms                                                                | 66.9 ms: 1.04x slower                                              |
| tomli_loads              | 2.09 sec                                                               | 2.17 sec: 1.04x slower                                             |
| regex_effbot             | 3.76 ms                                                                | 3.92 ms: 1.04x slower                                              |
| pyflate                  | 492 ms                                                                 | 513 ms: 1.04x slower                                               |
| pickle_list              | 4.96 us                                                                | 5.19 us: 1.05x slower                                              |
| mako                     | 10.9 ms                                                                | 11.4 ms: 1.05x slower                                              |
| pprint_safe_repr         | 756 ms                                                                 | 792 ms: 1.05x slower                                               |
| comprehensions           | 17.4 us                                                                | 18.3 us: 1.05x slower                                              |
| scimark_sparse_mat_mult  | 4.91 ms                                                                | 5.16 ms: 1.05x slower                                              |
| scimark_fft              | 339 ms                                                                 | 363 ms: 1.07x slower                                               |
| scimark_monte_carlo      | 70.2 ms                                                                | 75.1 ms: 1.07x slower                                              |
| regex_compile            | 144 ms                                                                 | 155 ms: 1.07x slower                                               |
| pprint_pformat           | 1.56 sec                                                               | 1.69 sec: 1.08x slower                                             |
| fannkuch                 | 398 ms                                                                 | 429 ms: 1.08x slower                                               |
| hexiom                   | 7.02 ms                                                                | 7.60 ms: 1.08x slower                                              |
| spectral_norm            | 113 ms                                                                 | 125 ms: 1.11x slower                                               |
| gc_traversal             | 3.58 ms                                                                | 4.09 ms: 1.14x slower                                              |
| unpack_sequence          | 86.4 ns                                                                | 122 ns: 1.41x slower                                               |
| Geometric mean           | (ref)                                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (27): djangocms, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, aiohttp, xml_etree_parse, xml_etree_process, json_dumps, asyncio_tcp, pathlib, dask, bench_thread_pool, asyncio_websockets, pickle_dict, unpickle, regex_v8, mypy2, gunicorn, logging_format, chameleon, sqlglot_normalize, tornado_http, sqlglot_parse, async_tree_memoization_tg, async_tree_memoization, logging_simple, pylint, async_tree_none


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.92x