# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_recompile
- machine: linux-x86_64
- commit hash: 0cc257c
- commit date: 2024-05-08
- overall geometric mean: 1.05x slower
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 302 ms: 1.10x slower                                                    |
| chameleon      | 7.41 ms                                                | 7.11 ms: 1.04x faster                                                   |
| docutils       | 2.77 sec                                               | 3.83 sec: 1.38x slower                                                  |
| tornado_http   | 103 ms                                                 | 99.4 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.16 sec                                               | 1.18 sec: 1.02x slower                                                  |
| async_tree_io_tg        | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                  |
| async_tree_none         | 472 ms                                                 | 489 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed | 726 ms                                                 | 754 ms: 1.04x slower                                                    |
| async_tree_none_tg      | 450 ms                                                 | 467 ms: 1.04x slower                                                    |
| async_tree_memoization  | 578 ms                                                 | 618 ms: 1.07x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                   |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                    |
| float          | 84.7 ms                                                | 89.8 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                    |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                    |
| regex_effbot   | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.05x faster                                                    |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                   |
| pickle_dict          | 35.5 us                                                | 34.2 us: 1.04x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.03x faster                                                    |
| unpickle_list        | 5.29 us                                                | 5.26 us: 1.01x faster                                                   |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                   |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                   |
| xml_etree_generate   | 89.2 ms                                                | 93.2 ms: 1.05x slower                                                   |
| xml_etree_process    | 61.7 ms                                                | 66.2 ms: 1.07x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.46 us: 1.07x slower                                                   |
| xml_etree_parse      | 159 ms                                                 | 174 ms: 1.09x slower                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 140 ms: 1.31x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.68 ms: 1.11x slower                                                   |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                   |
| django_template | 34.6 ms                                                | 36.4 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| comprehensions           | 21.8 us                                                | 16.8 us: 1.29x faster                                                   |
| mako                     | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                   |
| crypto_pyaes             | 81.9 ms                                                | 67.6 ms: 1.21x faster                                                   |
| scimark_fft              | 382 ms                                                 | 318 ms: 1.20x faster                                                    |
| nbody                    | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                   |
| scimark_monte_carlo      | 75.1 ms                                                | 64.1 ms: 1.17x faster                                                   |
| tomli_loads              | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                  |
| fannkuch                 | 417 ms                                                 | 363 ms: 1.15x faster                                                    |
| chaos                    | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                   |
| spectral_norm            | 115 ms                                                 | 102 ms: 1.13x faster                                                    |
| logging_format           | 7.23 us                                                | 6.45 us: 1.12x faster                                                   |
| logging_simple           | 6.46 us                                                | 5.77 us: 1.12x faster                                                   |
| raytrace                 | 312 ms                                                 | 280 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult  | 5.06 ms                                                | 4.54 ms: 1.11x faster                                                   |
| pyflate                  | 482 ms                                                 | 444 ms: 1.09x faster                                                    |
| pprint_safe_repr         | 776 ms                                                 | 714 ms: 1.09x faster                                                    |
| deepcopy_memo            | 40.7 us                                                | 37.7 us: 1.08x faster                                                   |
| pathlib                  | 19.3 ms                                                | 17.9 ms: 1.08x faster                                                   |
| regex_compile            | 148 ms                                                 | 140 ms: 1.06x faster                                                    |
| pprint_pformat           | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                  |
| pickle_pure_python       | 324 us                                                 | 307 us: 1.05x faster                                                    |
| generators               | 31.2 ms                                                | 29.9 ms: 1.05x faster                                                   |
| unpickle                 | 15.9 us                                                | 15.2 us: 1.04x faster                                                   |
| chameleon                | 7.41 ms                                                | 7.11 ms: 1.04x faster                                                   |
| richards                 | 45.8 ms                                                | 44.0 ms: 1.04x faster                                                   |
| pickle_dict              | 35.5 us                                                | 34.2 us: 1.04x faster                                                   |
| tornado_http             | 103 ms                                                 | 99.4 ms: 1.03x faster                                                   |
| meteor_contest           | 112 ms                                                 | 109 ms: 1.03x faster                                                    |
| unpickle_pure_python     | 230 us                                                 | 224 us: 1.03x faster                                                    |
| richards_super           | 51.5 ms                                                | 50.5 ms: 1.02x faster                                                   |
| unpickle_list            | 5.29 us                                                | 5.26 us: 1.01x faster                                                   |
| coroutines               | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                   |
| pidigits                 | 187 ms                                                 | 188 ms: 1.00x slower                                                    |
| json_loads               | 28.5 us                                                | 28.7 us: 1.01x slower                                                   |
| deepcopy                 | 371 us                                                 | 374 us: 1.01x slower                                                    |
| sqlite_synth             | 2.83 us                                                | 2.85 us: 1.01x slower                                                   |
| json                     | 5.26 ms                                                | 5.30 ms: 1.01x slower                                                   |
| deepcopy_reduce          | 3.35 us                                                | 3.39 us: 1.01x slower                                                   |
| dulwich_log              | 68.5 ms                                                | 69.4 ms: 1.01x slower                                                   |
| sympy_str                | 300 ms                                                 | 304 ms: 1.01x slower                                                    |
| async_tree_io            | 1.16 sec                                               | 1.18 sec: 1.02x slower                                                  |
| asyncio_websockets       | 551 ms                                                 | 564 ms: 1.02x slower                                                    |
| async_tree_io_tg         | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                  |
| sqlglot_parse            | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                   |
| sympy_sum                | 169 ms                                                 | 173 ms: 1.03x slower                                                    |
| hexiom                   | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                   |
| logging_silent           | 104 ns                                                 | 107 ns: 1.03x slower                                                    |
| sqlglot_transpile        | 1.68 ms                                                | 1.74 ms: 1.03x slower                                                   |
| bench_thread_pool        | 842 us                                                 | 871 us: 1.03x slower                                                    |
| pickle                   | 11.6 us                                                | 12.0 us: 1.04x slower                                                   |
| async_tree_none          | 472 ms                                                 | 489 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed  | 726 ms                                                 | 754 ms: 1.04x slower                                                    |
| async_tree_none_tg       | 450 ms                                                 | 467 ms: 1.04x slower                                                    |
| nqueens                  | 83.3 ms                                                | 86.6 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                  |
| sqlglot_normalize        | 110 ms                                                 | 115 ms: 1.04x slower                                                    |
| xml_etree_generate       | 89.2 ms                                                | 93.2 ms: 1.05x slower                                                   |
| asyncio_tcp              | 491 ms                                                 | 515 ms: 1.05x slower                                                    |
| django_template          | 34.6 ms                                                | 36.4 ms: 1.05x slower                                                   |
| async_generators         | 463 ms                                                 | 488 ms: 1.05x slower                                                    |
| scimark_lu               | 118 ms                                                 | 125 ms: 1.06x slower                                                    |
| regex_dna                | 212 ms                                                 | 224 ms: 1.06x slower                                                    |
| float                    | 84.7 ms                                                | 89.8 ms: 1.06x slower                                                   |
| mdp                      | 2.63 sec                                               | 2.80 sec: 1.06x slower                                                  |
| sympy_integrate          | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                   |
| regex_effbot             | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                   |
| async_tree_memoization   | 578 ms                                                 | 618 ms: 1.07x slower                                                    |
| pycparser                | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                  |
| xml_etree_process        | 61.7 ms                                                | 66.2 ms: 1.07x slower                                                   |
| sqlglot_optimize         | 54.8 ms                                                | 58.8 ms: 1.07x slower                                                   |
| sympy_expand             | 478 ms                                                 | 513 ms: 1.07x slower                                                    |
| pickle_list              | 5.08 us                                                | 5.46 us: 1.07x slower                                                   |
| deltablue                | 3.72 ms                                                | 3.99 ms: 1.07x slower                                                   |
| go                       | 139 ms                                                 | 151 ms: 1.08x slower                                                    |
| xml_etree_parse          | 159 ms                                                 | 174 ms: 1.09x slower                                                    |
| 2to3                     | 274 ms                                                 | 302 ms: 1.10x slower                                                    |
| python_startup_no_site   | 6.94 ms                                                | 7.68 ms: 1.11x slower                                                   |
| gunicorn                 | 1.24 ms                                                | 1.38 ms: 1.11x slower                                                   |
| typing_runtime_protocols | 158 us                                                 | 175 us: 1.11x slower                                                    |
| aiohttp                  | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                   |
| regex_v8                 | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                   |
| gc_traversal             | 3.79 ms                                                | 4.32 ms: 1.14x slower                                                   |
| python_startup           | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                   |
| dask                     | 372 ms                                                 | 449 ms: 1.21x slower                                                    |
| coverage                 | 72.7 ms                                                | 89.6 ms: 1.23x slower                                                   |
| xml_etree_iterparse      | 107 ms                                                 | 140 ms: 1.31x slower                                                    |
| docutils                 | 2.77 sec                                               | 3.83 sec: 1.38x slower                                                  |
| create_gc_cycles         | 1.48 ms                                                | 2.23 ms: 1.51x slower                                                   |
| telco                    | 7.10 ms                                                | 170 ms: 24.00x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.05x slower                                                            |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, json_dumps, scimark_sor, bench_mp_pool, async_tree_memoization_tg
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240508-3.14.0a0-0cc257c-JIT/bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.24% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x