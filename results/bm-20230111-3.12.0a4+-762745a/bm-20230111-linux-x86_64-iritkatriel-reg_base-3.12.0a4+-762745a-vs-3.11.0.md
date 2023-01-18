
# Results vs. 3.11.0

- fork: iritkatriel
- ref: reg_base
- machine: linux-x86_64
- commit hash: 762745a
- commit date: 2023-01-11
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                            |
| chameleon      | 6.41 ms                                                | 6.30 ms: 1.02x faster                                           |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                          |
| html5lib       | 63.2 ms                                                | 59.5 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.3 ms: 1.06x faster                                           |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                            |
| regex_dna      | 203 ms                                                 | 202 ms: 1.01x faster                                            |
| regex_effbot   | 3.36 ms                                                | 3.38 ms: 1.01x slower                                           |
| regex_v8       | 22.3 ms                                                | 20.7 ms: 1.08x faster                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.52 ms: 1.33x faster                                           |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                           |
| pickle               | 9.79 us                                                | 10.0 us: 1.03x slower                                           |
| pickle_dict          | 31.4 us                                                | 29.6 us: 1.06x faster                                           |
| pickle_list          | 4.17 us                                                | 3.97 us: 1.05x faster                                           |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.08x faster                                            |
| unpickle             | 13.3 us                                                | 12.9 us: 1.03x faster                                           |
| unpickle_list        | 4.95 us                                                | 4.85 us: 1.02x faster                                           |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.15x faster                                            |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                            |
| xml_etree_iterparse  | 103 ms                                                 | 104 ms: 1.02x slower                                            |
| xml_etree_generate   | 76.2 ms                                                | 76.8 ms: 1.01x slower                                           |
| xml_etree_process    | 53.8 ms                                                | 54.0 ms: 1.00x slower                                           |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.51 ms: 1.02x slower                                           |
| python_startup_no_site | 5.96 ms                                                | 6.07 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text    | 22.1 ms                                                | 20.2 ms: 1.10x faster                                           |
| genshi_xml     | 52.1 ms                                                | 46.6 ms: 1.12x faster                                           |
| mako           | 9.85 ms                                                | 9.66 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                            |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                            |
| async_tree_none         | 529 ms                                                 | 522 ms: 1.01x faster                                            |
| async_tree_memoization  | 625 ms                                                 | 639 ms: 1.02x slower                                            |
| chameleon               | 6.41 ms                                                | 6.30 ms: 1.02x faster                                           |
| chaos                   | 68.6 ms                                                | 68.2 ms: 1.01x faster                                           |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                            |
| coroutines              | 26.1 ms                                                | 24.6 ms: 1.06x faster                                           |
| coverage                | 101 ms                                                 | 99.3 ms: 1.01x faster                                           |
| deepcopy                | 344 us                                                 | 334 us: 1.03x faster                                            |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.07x faster                                           |
| deltablue               | 3.64 ms                                                | 3.24 ms: 1.12x faster                                           |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                          |
| dulwich_log             | 63.9 ms                                                | 61.5 ms: 1.04x faster                                           |
| fannkuch                | 388 ms                                                 | 358 ms: 1.09x faster                                            |
| float                   | 76.3 ms                                                | 72.3 ms: 1.06x faster                                           |
| generators              | 72.2 ms                                                | 79.0 ms: 1.09x slower                                           |
| genshi_text             | 22.1 ms                                                | 20.2 ms: 1.10x faster                                           |
| genshi_xml              | 52.1 ms                                                | 46.6 ms: 1.12x faster                                           |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                            |
| hexiom                  | 6.35 ms                                                | 6.08 ms: 1.04x faster                                           |
| html5lib                | 63.2 ms                                                | 59.5 ms: 1.06x faster                                           |
| json                    | 4.95 ms                                                | 4.69 ms: 1.05x faster                                           |
| json_dumps              | 12.7 ms                                                | 9.52 ms: 1.33x faster                                           |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                           |
| logging_format          | 6.62 us                                                | 6.26 us: 1.06x faster                                           |
| logging_silent          | 98.5 ns                                                | 93.7 ns: 1.05x faster                                           |
| logging_simple          | 6.06 us                                                | 5.69 us: 1.07x faster                                           |
| mako                    | 9.85 ms                                                | 9.66 ms: 1.02x faster                                           |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                          |
| mypy                    | 669 ms                                                 | 808 ms: 1.21x slower                                            |
| nqueens                 | 85.0 ms                                                | 78.2 ms: 1.09x faster                                           |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                           |
| pickle                  | 9.79 us                                                | 10.0 us: 1.03x slower                                           |
| pickle_dict             | 31.4 us                                                | 29.6 us: 1.06x faster                                           |
| pickle_list             | 4.17 us                                                | 3.97 us: 1.05x faster                                           |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.08x faster                                            |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                            |
| pprint_safe_repr        | 691 ms                                                 | 669 ms: 1.03x faster                                            |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                          |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.07x faster                                          |
| pyflate                 | 417 ms                                                 | 393 ms: 1.06x faster                                            |
| python_startup          | 8.36 ms                                                | 8.51 ms: 1.02x slower                                           |
| python_startup_no_site  | 5.96 ms                                                | 6.07 ms: 1.02x slower                                           |
| raytrace                | 290 ms                                                 | 287 ms: 1.01x faster                                            |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                            |
| regex_dna               | 203 ms                                                 | 202 ms: 1.01x faster                                            |
| regex_effbot            | 3.36 ms                                                | 3.38 ms: 1.01x slower                                           |
| regex_v8                | 22.3 ms                                                | 20.7 ms: 1.08x faster                                           |
| richards                | 46.2 ms                                                | 43.0 ms: 1.07x faster                                           |
| scimark_fft             | 329 ms                                                 | 310 ms: 1.06x faster                                            |
| scimark_monte_carlo     | 68.3 ms                                                | 64.4 ms: 1.06x faster                                           |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                            |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.09 ms: 1.07x faster                                           |
| spectral_norm           | 99.9 ms                                                | 94.6 ms: 1.06x faster                                           |
| sqlglot_parse           | 1.37 ms                                                | 1.39 ms: 1.01x slower                                           |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                           |
| sqlglot_optimize        | 53.0 ms                                                | 50.9 ms: 1.04x faster                                           |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                            |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                           |
| sympy_expand            | 472 ms                                                 | 456 ms: 1.03x faster                                            |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                           |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                            |
| sympy_str               | 287 ms                                                 | 283 ms: 1.02x faster                                            |
| telco                   | 6.62 ms                                                | 6.32 ms: 1.05x faster                                           |
| thrift                  | 752 us                                                 | 764 us: 1.02x slower                                            |
| unpack_sequence         | 43.4 ns                                                | 41.4 ns: 1.05x faster                                           |
| unpickle                | 13.3 us                                                | 12.9 us: 1.03x faster                                           |
| unpickle_list           | 4.95 us                                                | 4.85 us: 1.02x faster                                           |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.15x faster                                            |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                            |
| xml_etree_iterparse     | 103 ms                                                 | 104 ms: 1.02x slower                                            |
| xml_etree_generate      | 76.2 ms                                                | 76.8 ms: 1.01x slower                                           |
| xml_etree_process       | 53.8 ms                                                | 54.0 ms: 1.00x slower                                           |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_io, bench_mp_pool, crypto_pyaes, deepcopy_reduce, django_template, meteor_contest, nbody, scimark_lu
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230111-3.12.0a4+-762745a/bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
