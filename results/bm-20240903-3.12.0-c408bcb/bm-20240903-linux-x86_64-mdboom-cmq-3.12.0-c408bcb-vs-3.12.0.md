# Results vs. 3.12.0

- fork: mdboom
- ref: cmq
- machine: linux-x86_64
- commit hash: c408bcb
- commit date: 2024-09-03
- overall geometric mean: 1.00x faster
- HPT reliability: 80.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------|:------------------------------------------------------:|:--------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                               |
| chameleon      | 7.41 ms                                                | 7.26 ms: 1.02x faster                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                       |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|--------------------|:------------------------------------------------------:|:--------------------------------------------------:|
| async_tree_none_tg | 450 ms                                                 | 445 ms: 1.01x faster                               |
| async_tree_io      | 1.16 sec                                               | 1.16 sec: 1.00x slower                             |
| async_tree_io_tg   | 1.18 sec                                               | 1.19 sec: 1.01x slower                             |
| Geometric mean     | (ref)                                                  | 1.00x faster                                       |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------|:------------------------------------------------------:|:--------------------------------------------------:|
| nbody          | 97.0 ms                                                | 92.0 ms: 1.05x faster                              |
| float          | 84.7 ms                                                | 83.1 ms: 1.02x faster                              |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------|:------------------------------------------------------:|:--------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                               |
| regex_compile  | 148 ms                                                 | 149 ms: 1.01x slower                               |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                              |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------:|
| pickle_dict          | 35.5 us                                                | 33.3 us: 1.07x faster                              |
| tomli_loads          | 2.33 sec                                               | 2.26 sec: 1.03x faster                             |
| pickle_list          | 5.08 us                                                | 4.94 us: 1.03x faster                              |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                              |
| xml_etree_generate   | 89.2 ms                                                | 88.1 ms: 1.01x faster                              |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                              |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                               |
| xml_etree_process    | 61.7 ms                                                | 61.4 ms: 1.01x faster                              |
| unpickle_pure_python | 230 us                                                 | 230 us: 1.00x faster                               |
| unpickle_list        | 5.29 us                                                | 5.41 us: 1.02x slower                              |
| Geometric mean       | (ref)                                                  | 1.01x faster                                       |

Benchmark hidden because not significant (4): json_dumps, xml_etree_parse, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x slower                              |
| python_startup         | 9.55 ms                                                | 9.60 ms: 1.00x slower                              |
| Geometric mean         | (ref)                                                  | 1.00x slower                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------|:------------------------------------------------------:|:--------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.4 ms: 1.04x faster                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------:|
| unpack_sequence          | 54.0 ns                                                | 50.1 ns: 1.08x faster                              |
| pickle_dict              | 35.5 us                                                | 33.3 us: 1.07x faster                              |
| nbody                    | 97.0 ms                                                | 92.0 ms: 1.05x faster                              |
| spectral_norm            | 115 ms                                                 | 110 ms: 1.04x faster                               |
| mako                     | 11.9 ms                                                | 11.4 ms: 1.04x faster                              |
| tomli_loads              | 2.33 sec                                               | 2.26 sec: 1.03x faster                             |
| pickle_list              | 5.08 us                                                | 4.94 us: 1.03x faster                              |
| chameleon                | 7.41 ms                                                | 7.26 ms: 1.02x faster                              |
| float                    | 84.7 ms                                                | 83.1 ms: 1.02x faster                              |
| json_loads               | 28.5 us                                                | 28.0 us: 1.02x faster                              |
| meteor_contest           | 112 ms                                                 | 111 ms: 1.02x faster                               |
| pprint_safe_repr         | 776 ms                                                 | 763 ms: 1.02x faster                               |
| deepcopy_reduce          | 3.35 us                                                | 3.29 us: 1.02x faster                              |
| mdp                      | 2.63 sec                                               | 2.59 sec: 1.01x faster                             |
| regex_dna                | 212 ms                                                 | 209 ms: 1.01x faster                               |
| deepcopy_memo            | 40.7 us                                                | 40.2 us: 1.01x faster                              |
| sqlite_synth             | 2.83 us                                                | 2.80 us: 1.01x faster                              |
| xml_etree_generate       | 89.2 ms                                                | 88.1 ms: 1.01x faster                              |
| sympy_sum                | 169 ms                                                 | 167 ms: 1.01x faster                               |
| pickle                   | 11.6 us                                                | 11.5 us: 1.01x faster                              |
| deepcopy                 | 371 us                                                 | 367 us: 1.01x faster                               |
| coroutines               | 23.2 ms                                                | 22.9 ms: 1.01x faster                              |
| async_generators         | 463 ms                                                 | 459 ms: 1.01x faster                               |
| async_tree_none_tg       | 450 ms                                                 | 445 ms: 1.01x faster                               |
| raytrace                 | 312 ms                                                 | 309 ms: 1.01x faster                               |
| create_gc_cycles         | 1.48 ms                                                | 1.46 ms: 1.01x faster                              |
| pyflate                  | 482 ms                                                 | 478 ms: 1.01x faster                               |
| pprint_pformat           | 1.57 sec                                               | 1.56 sec: 1.01x faster                             |
| xml_etree_iterparse      | 107 ms                                                 | 106 ms: 1.01x faster                               |
| comprehensions           | 21.8 us                                                | 21.6 us: 1.01x faster                              |
| typing_runtime_protocols | 158 us                                                 | 157 us: 1.01x faster                               |
| pycparser                | 1.18 sec                                               | 1.17 sec: 1.01x faster                             |
| xml_etree_process        | 61.7 ms                                                | 61.4 ms: 1.01x faster                              |
| sympy_integrate          | 21.4 ms                                                | 21.3 ms: 1.00x faster                              |
| pidigits                 | 187 ms                                                 | 187 ms: 1.00x faster                               |
| unpickle_pure_python     | 230 us                                                 | 230 us: 1.00x faster                               |
| python_startup_no_site   | 6.94 ms                                                | 6.94 ms: 1.00x slower                              |
| async_tree_io            | 1.16 sec                                               | 1.16 sec: 1.00x slower                             |
| sqlglot_optimize         | 54.8 ms                                                | 54.9 ms: 1.00x slower                              |
| dulwich_log              | 68.5 ms                                                | 68.7 ms: 1.00x slower                              |
| go                       | 139 ms                                                 | 140 ms: 1.00x slower                               |
| scimark_lu               | 118 ms                                                 | 119 ms: 1.00x slower                               |
| python_startup           | 9.55 ms                                                | 9.60 ms: 1.00x slower                              |
| gc_traversal             | 3.79 ms                                                | 3.81 ms: 1.01x slower                              |
| aiohttp                  | 1.15 ms                                                | 1.16 ms: 1.01x slower                              |
| 2to3                     | 274 ms                                                 | 276 ms: 1.01x slower                               |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.80 sec: 1.01x slower                             |
| scimark_monte_carlo      | 75.1 ms                                                | 75.6 ms: 1.01x slower                              |
| fannkuch                 | 417 ms                                                 | 420 ms: 1.01x slower                               |
| regex_compile            | 148 ms                                                 | 149 ms: 1.01x slower                               |
| deltablue                | 3.72 ms                                                | 3.74 ms: 1.01x slower                              |
| chaos                    | 67.0 ms                                                | 67.5 ms: 1.01x slower                              |
| async_tree_io_tg         | 1.18 sec                                               | 1.19 sec: 1.01x slower                             |
| regex_effbot             | 3.61 ms                                                | 3.64 ms: 1.01x slower                              |
| bench_thread_pool        | 842 us                                                 | 851 us: 1.01x slower                               |
| coverage                 | 72.7 ms                                                | 73.9 ms: 1.02x slower                              |
| logging_silent           | 104 ns                                                 | 106 ns: 1.02x slower                               |
| pathlib                  | 19.3 ms                                                | 19.7 ms: 1.02x slower                              |
| richards                 | 45.8 ms                                                | 46.6 ms: 1.02x slower                              |
| richards_super           | 51.5 ms                                                | 52.4 ms: 1.02x slower                              |
| nqueens                  | 83.3 ms                                                | 84.9 ms: 1.02x slower                              |
| crypto_pyaes             | 81.9 ms                                                | 83.5 ms: 1.02x slower                              |
| scimark_sor              | 129 ms                                                 | 132 ms: 1.02x slower                               |
| hexiom                   | 6.41 ms                                                | 6.55 ms: 1.02x slower                              |
| unpickle_list            | 5.29 us                                                | 5.41 us: 1.02x slower                              |
| regex_v8                 | 23.1 ms                                                | 24.0 ms: 1.04x slower                              |
| scimark_sparse_mat_mult  | 5.06 ms                                                | 5.26 ms: 1.04x slower                              |
| asyncio_tcp              | 491 ms                                                 | 514 ms: 1.05x slower                               |
| generators               | 31.2 ms                                                | 33.6 ms: 1.08x slower                              |
| Geometric mean           | (ref)                                                  | 1.00x faster                                       |

Benchmark hidden because not significant (29): async_tree_cpu_io_mixed_tg, sqlalchemy_imperative, async_tree_cpu_io_mixed, telco, dask, async_tree_memoization_tg, json, django_template, sqlglot_parse, json_dumps, docutils, sqlglot_transpile, logging_format, asyncio_websockets, bench_mp_pool, async_tree_none, sqlglot_normalize, sympy_expand, sqlalchemy_declarative, tornado_http, scimark_fft, sympy_str, gunicorn, xml_etree_parse, async_tree_memoization, pickle_pure_python, logging_simple, unpickle, mypy2
Ignored benchmarks (8) of results/bm-20240903-3.12.0-c408bcb/bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 80.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.57x