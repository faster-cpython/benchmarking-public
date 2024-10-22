# Results vs. 3.12.0

- fork: python
- ref: df13a1821a90fcfb75ec
- machine: linux-x86_64
- commit hash: df13a18
- commit date: 2024-08-01
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| tornado_http   | 103 ms                                                 | 92.3 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 871 ms: 1.36x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 910 ms: 1.27x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.8 ms: 1.21x faster                                                 |
| float          | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.8 ms: 1.07x faster                                                 |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                 |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                 |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 871 ms: 1.36x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 910 ms: 1.27x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 60.9 ms: 1.23x faster                                                 |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 67.4 ms: 1.22x faster                                                 |
| nbody                      | 97.0 ms                                                | 79.8 ms: 1.21x faster                                                 |
| mako                       | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.24 ms: 1.19x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.82 us: 1.19x faster                                                 |
| float                      | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                 |
| chaos                      | 67.0 ms                                                | 57.8 ms: 1.16x faster                                                 |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                  |
| fannkuch                   | 417 ms                                                 | 369 ms: 1.13x faster                                                  |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                  |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.12x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                 |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                                  |
| tornado_http               | 103 ms                                                 | 92.3 ms: 1.11x faster                                                 |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                  |
| richards_super             | 51.5 ms                                                | 46.8 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                  |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.8 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.60 ms: 1.03x faster                                                 |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                 |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.74 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                  |
| async_generators           | 463 ms                                                 | 466 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                 |
| nqueens                    | 83.3 ms                                                | 86.4 ms: 1.04x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.73 ms: 1.05x slower                                                 |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                 |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                  |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                 |
| coverage                   | 72.7 ms                                                | 91.3 ms: 1.26x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (7): pycparser, mdp, json_dumps, asyncio_tcp, sympy_str, bench_mp_pool, 2to3
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240801-3.14.0a0-df13a18-JIT/bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x