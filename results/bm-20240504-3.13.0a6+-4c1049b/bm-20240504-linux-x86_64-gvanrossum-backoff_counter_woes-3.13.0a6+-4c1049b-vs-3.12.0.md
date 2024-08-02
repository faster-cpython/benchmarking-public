# Results vs. 3.12.0

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.03x faster
- HPT reliability: 99.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                       |
| chameleon      | 7.41 ms                                                | 7.15 ms: 1.04x faster                                                      |
| docutils       | 2.77 sec                                               | 2.83 sec: 1.02x slower                                                     |
| tornado_http   | 103 ms                                                 | 94.7 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 928 ms: 1.27x faster                                                       |
| async_tree_none            | 472 ms                                                 | 370 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 582 ms: 1.25x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 466 ms: 1.24x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 628 ms: 1.16x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                      |
| nbody          | 97.0 ms                                                | 90.4 ms: 1.07x faster                                                      |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                      |
| regex_dna      | 212 ms                                                 | 232 ms: 1.09x slower                                                       |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                     |
| unpickle             | 15.9 us                                                | 15.3 us: 1.03x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                       |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.00 us: 1.02x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 61.0 ms: 1.01x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 88.1 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 107 ms: 1.01x slower                                                       |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                      |
| pickle_dict          | 35.5 us                                                | 36.4 us: 1.03x slower                                                      |
| unpickle_list        | 5.29 us                                                | 5.44 us: 1.03x slower                                                      |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.21 ms: 1.04x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                      |
| django_template | 34.6 ms                                                | 35.1 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 928 ms: 1.27x faster                                                       |
| async_tree_none            | 472 ms                                                 | 370 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 582 ms: 1.25x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 466 ms: 1.24x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                       |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 628 ms: 1.16x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                      |
| logging_format             | 7.23 us                                                | 6.46 us: 1.12x faster                                                      |
| mypy2                      | 830 ms                                                 | 744 ms: 1.12x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.82 us: 1.11x faster                                                      |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                      |
| pathlib                    | 19.3 ms                                                | 17.5 ms: 1.11x faster                                                      |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                       |
| tornado_http               | 103 ms                                                 | 94.7 ms: 1.08x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                       |
| float                      | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 69.6 ms: 1.08x faster                                                      |
| nbody                      | 97.0 ms                                                | 90.4 ms: 1.07x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                     |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 76.9 ms: 1.06x faster                                                      |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                      |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                                       |
| async_generators           | 463 ms                                                 | 444 ms: 1.04x faster                                                       |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                       |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                                      |
| chameleon                  | 7.41 ms                                                | 7.15 ms: 1.04x faster                                                      |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.03x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 66.6 ms: 1.03x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 755 ms: 1.03x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                      |
| scimark_fft                | 382 ms                                                 | 372 ms: 1.03x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.02x faster                                                      |
| deepcopy                   | 371 us                                                 | 363 us: 1.02x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                                       |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 3.29 us: 1.02x faster                                                      |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                       |
| pickle_list                | 5.08 us                                                | 5.00 us: 1.02x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 61.0 ms: 1.01x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 88.1 ms: 1.01x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 40.2 us: 1.01x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                       |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                       |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 107 ms: 1.01x slower                                                       |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                      |
| django_template            | 34.6 ms                                                | 35.1 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                       |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                                       |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                       |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.83 sec: 1.02x slower                                                     |
| pickle_dict                | 35.5 us                                                | 36.4 us: 1.03x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                       |
| unpickle_list              | 5.29 us                                                | 5.44 us: 1.03x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 506 ms: 1.03x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                     |
| aiohttp                    | 1.15 ms                                                | 1.19 ms: 1.03x slower                                                      |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                       |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                      |
| gunicorn                   | 1.24 ms                                                | 1.29 ms: 1.04x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.21 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.29 ms: 1.05x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 3.99 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                       |
| regex_dna                  | 212 ms                                                 | 232 ms: 1.09x slower                                                       |
| richards_super             | 51.5 ms                                                | 56.4 ms: 1.09x slower                                                      |
| richards                   | 45.8 ms                                                | 50.4 ms: 1.10x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                      |
| telco                      | 7.10 ms                                                | 8.60 ms: 1.21x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.84 ms: 1.25x slower                                                      |
| coverage                   | 72.7 ms                                                | 94.7 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (5): xml_etree_parse, dask, sympy_expand, nqueens, json
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x