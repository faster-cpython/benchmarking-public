# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.010x faster
- HPT reliability: 81.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                       |
| chameleon      | 7.41 ms                                                | 6.93 ms: 1.07x faster                                      |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                     |
| tornado_http   | 103 ms                                                 | 96.9 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 472 ms                                                 | 438 ms: 1.08x faster                                       |
| async_tree_cpu_io_mixed | 726 ms                                                 | 710 ms: 1.02x faster                                       |
| async_tree_memoization  | 578 ms                                                 | 565 ms: 1.02x faster                                       |
| async_tree_none_tg      | 450 ms                                                 | 448 ms: 1.00x faster                                       |
| async_tree_io_tg        | 1.18 sec                                               | 1.20 sec: 1.02x slower                                     |
| async_tree_io           | 1.16 sec                                               | 1.18 sec: 1.02x slower                                     |
| Geometric mean          | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| float          | 84.7 ms                                                | 85.3 ms: 1.01x slower                                      |
| nbody          | 97.0 ms                                                | 103 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.59 ms: 1.01x faster                                      |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python | 324 us                                                 | 298 us: 1.09x faster                                       |
| unpickle_list      | 5.29 us                                                | 4.96 us: 1.07x faster                                      |
| xml_etree_process  | 61.7 ms                                                | 58.4 ms: 1.06x faster                                      |
| tomli_loads        | 2.33 sec                                               | 2.21 sec: 1.05x faster                                     |
| pickle_dict        | 35.5 us                                                | 34.2 us: 1.04x faster                                      |
| unpickle           | 15.9 us                                                | 15.3 us: 1.04x faster                                      |
| json_loads         | 28.5 us                                                | 27.5 us: 1.04x faster                                      |
| xml_etree_generate | 89.2 ms                                                | 86.0 ms: 1.04x faster                                      |
| xml_etree_parse    | 159 ms                                                 | 156 ms: 1.02x faster                                       |
| pickle             | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| pickle_list        | 5.08 us                                                | 5.00 us: 1.02x faster                                      |
| Geometric mean     | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.2 ms: 1.07x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 8.84 ms: 1.27x slower                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                      |
| mako            | 11.9 ms                                                | 12.1 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 158 us                                                 | 111 us: 1.42x faster                                       |
| comprehensions           | 21.8 us                                                | 18.3 us: 1.19x faster                                      |
| raytrace                 | 312 ms                                                 | 279 ms: 1.12x faster                                       |
| logging_format           | 7.23 us                                                | 6.47 us: 1.12x faster                                      |
| logging_simple           | 6.46 us                                                | 5.81 us: 1.11x faster                                      |
| deepcopy_reduce          | 3.35 us                                                | 3.03 us: 1.10x faster                                      |
| deltablue                | 3.72 ms                                                | 3.37 ms: 1.10x faster                                      |
| pickle_pure_python       | 324 us                                                 | 298 us: 1.09x faster                                       |
| scimark_sor              | 129 ms                                                 | 119 ms: 1.08x faster                                       |
| regex_compile            | 148 ms                                                 | 138 ms: 1.08x faster                                       |
| async_tree_none          | 472 ms                                                 | 438 ms: 1.08x faster                                       |
| generators               | 31.2 ms                                                | 29.2 ms: 1.07x faster                                      |
| chameleon                | 7.41 ms                                                | 6.93 ms: 1.07x faster                                      |
| sympy_sum                | 169 ms                                                 | 159 ms: 1.07x faster                                       |
| unpickle_list            | 5.29 us                                                | 4.96 us: 1.07x faster                                      |
| sqlglot_parse            | 1.36 ms                                                | 1.28 ms: 1.06x faster                                      |
| deepcopy                 | 371 us                                                 | 350 us: 1.06x faster                                       |
| tornado_http             | 103 ms                                                 | 96.9 ms: 1.06x faster                                      |
| sympy_str                | 300 ms                                                 | 283 ms: 1.06x faster                                       |
| deepcopy_memo            | 40.7 us                                                | 38.5 us: 1.06x faster                                      |
| xml_etree_process        | 61.7 ms                                                | 58.4 ms: 1.06x faster                                      |
| tomli_loads              | 2.33 sec                                               | 2.21 sec: 1.05x faster                                     |
| pathlib                  | 19.3 ms                                                | 18.4 ms: 1.05x faster                                      |
| docutils                 | 2.77 sec                                               | 2.64 sec: 1.05x faster                                     |
| sqlglot_transpile        | 1.68 ms                                                | 1.61 ms: 1.05x faster                                      |
| crypto_pyaes             | 81.9 ms                                                | 78.6 ms: 1.04x faster                                      |
| sympy_integrate          | 21.4 ms                                                | 20.6 ms: 1.04x faster                                      |
| pickle_dict              | 35.5 us                                                | 34.2 us: 1.04x faster                                      |
| meteor_contest           | 112 ms                                                 | 108 ms: 1.04x faster                                       |
| unpickle                 | 15.9 us                                                | 15.3 us: 1.04x faster                                      |
| json_loads               | 28.5 us                                                | 27.5 us: 1.04x faster                                      |
| json                     | 5.26 ms                                                | 5.07 ms: 1.04x faster                                      |
| xml_etree_generate       | 89.2 ms                                                | 86.0 ms: 1.04x faster                                      |
| scimark_fft              | 382 ms                                                 | 369 ms: 1.03x faster                                       |
| logging_silent           | 104 ns                                                 | 101 ns: 1.03x faster                                       |
| asyncio_tcp              | 491 ms                                                 | 478 ms: 1.03x faster                                       |
| unpack_sequence          | 54.0 ns                                                | 52.6 ns: 1.03x faster                                      |
| coroutines               | 23.2 ms                                                | 22.6 ms: 1.02x faster                                      |
| async_tree_cpu_io_mixed  | 726 ms                                                 | 710 ms: 1.02x faster                                       |
| async_tree_memoization   | 578 ms                                                 | 565 ms: 1.02x faster                                       |
| gc_traversal             | 3.79 ms                                                | 3.72 ms: 1.02x faster                                      |
| xml_etree_parse          | 159 ms                                                 | 156 ms: 1.02x faster                                       |
| pickle                   | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| async_generators         | 463 ms                                                 | 455 ms: 1.02x faster                                       |
| sqlglot_normalize        | 110 ms                                                 | 108 ms: 1.02x faster                                       |
| pickle_list              | 5.08 us                                                | 5.00 us: 1.02x faster                                      |
| richards                 | 45.8 ms                                                | 45.3 ms: 1.01x faster                                      |
| django_template          | 34.6 ms                                                | 34.2 ms: 1.01x faster                                      |
| scimark_lu               | 118 ms                                                 | 117 ms: 1.01x faster                                       |
| scimark_monte_carlo      | 75.1 ms                                                | 74.5 ms: 1.01x faster                                      |
| pprint_safe_repr         | 776 ms                                                 | 770 ms: 1.01x faster                                       |
| regex_effbot             | 3.61 ms                                                | 3.59 ms: 1.01x faster                                      |
| async_tree_none_tg       | 450 ms                                                 | 448 ms: 1.00x faster                                       |
| bench_thread_pool        | 842 us                                                 | 839 us: 1.00x faster                                       |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.79 sec: 1.00x slower                                     |
| pidigits                 | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| float                    | 84.7 ms                                                | 85.3 ms: 1.01x slower                                      |
| fannkuch                 | 417 ms                                                 | 420 ms: 1.01x slower                                       |
| 2to3                     | 274 ms                                                 | 277 ms: 1.01x slower                                       |
| sympy_expand             | 478 ms                                                 | 484 ms: 1.01x slower                                       |
| mako                     | 11.9 ms                                                | 12.1 ms: 1.02x slower                                      |
| sqlglot_optimize         | 54.8 ms                                                | 55.7 ms: 1.02x slower                                      |
| async_tree_io_tg         | 1.18 sec                                               | 1.20 sec: 1.02x slower                                     |
| regex_dna                | 212 ms                                                 | 216 ms: 1.02x slower                                       |
| async_tree_io            | 1.16 sec                                               | 1.18 sec: 1.02x slower                                     |
| gunicorn                 | 1.24 ms                                                | 1.27 ms: 1.02x slower                                      |
| aiohttp                  | 1.15 ms                                                | 1.18 ms: 1.02x slower                                      |
| mdp                      | 2.63 sec                                               | 2.71 sec: 1.03x slower                                     |
| chaos                    | 67.0 ms                                                | 69.5 ms: 1.04x slower                                      |
| pprint_pformat           | 1.57 sec                                               | 1.63 sec: 1.04x slower                                     |
| scimark_sparse_mat_mult  | 5.06 ms                                                | 5.30 ms: 1.05x slower                                      |
| pyflate                  | 482 ms                                                 | 507 ms: 1.05x slower                                       |
| go                       | 139 ms                                                 | 148 ms: 1.06x slower                                       |
| nbody                    | 97.0 ms                                                | 103 ms: 1.07x slower                                       |
| python_startup           | 9.55 ms                                                | 10.2 ms: 1.07x slower                                      |
| regex_v8                 | 23.1 ms                                                | 25.2 ms: 1.09x slower                                      |
| nqueens                  | 83.3 ms                                                | 91.0 ms: 1.09x slower                                      |
| spectral_norm            | 115 ms                                                 | 132 ms: 1.15x slower                                       |
| telco                    | 7.10 ms                                                | 8.42 ms: 1.19x slower                                      |
| hexiom                   | 6.41 ms                                                | 7.76 ms: 1.21x slower                                      |
| python_startup_no_site   | 6.94 ms                                                | 8.84 ms: 1.27x slower                                      |
| coverage                 | 72.7 ms                                                | 94.7 ms: 1.30x slower                                      |
| Geometric mean           | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed_tg, unpickle_pure_python, sqlite_synth, bench_mp_pool, json_dumps, xml_etree_iterparse, create_gc_cycles, dulwich_log, asyncio_websockets, async_tree_memoization_tg, richards_super, pycparser, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 81.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x