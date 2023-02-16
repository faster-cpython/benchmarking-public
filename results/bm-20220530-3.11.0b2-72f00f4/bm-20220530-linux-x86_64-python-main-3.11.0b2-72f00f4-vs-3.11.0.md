
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| chameleon      | 6.38 ms                                                | 6.59 ms: 1.03x slower                                 |
| html5lib       | 64.8 ms                                                | 63.8 ms: 1.02x faster                                 |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.05x faster                                 |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                  |
| nbody          | 90.0 ms                                                | 90.9 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.02 ms: 1.15x faster                                 |
| regex_dna      | 203 ms                                                 | 196 ms: 1.04x faster                                  |
| regex_v8       | 22.2 ms                                                | 21.5 ms: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|--------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict        | 31.2 us                                                | 25.9 us: 1.20x faster                                 |
| json_loads         | 26.1 us                                                | 24.3 us: 1.07x faster                                 |
| pickle             | 9.90 us                                                | 9.61 us: 1.03x faster                                 |
| pickle_pure_python | 308 us                                                 | 302 us: 1.02x faster                                  |
| xml_etree_parse    | 160 ms                                                 | 157 ms: 1.02x faster                                  |
| xml_etree_process  | 53.7 ms                                                | 53.3 ms: 1.01x faster                                 |
| json_dumps         | 12.4 ms                                                | 12.6 ms: 1.02x slower                                 |
| pickle_list        | 4.14 us                                                | 4.30 us: 1.04x slower                                 |
| Geometric mean     | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (5): xml_etree_iterparse, unpickle_list, xml_etree_generate, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.33 ms: 1.03x faster                                 |
| python_startup_no_site | 6.04 ms                                                | 6.17 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako           | 9.83 ms                                                | 9.71 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 31.2 us                                                | 25.9 us: 1.20x faster                                 |
| regex_effbot            | 3.46 ms                                                | 3.02 ms: 1.15x faster                                 |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.07x faster                                |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                 |
| float                   | 76.8 ms                                                | 72.8 ms: 1.05x faster                                 |
| sympy_sum               | 166 ms                                                 | 159 ms: 1.04x faster                                  |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                  |
| regex_dna               | 203 ms                                                 | 196 ms: 1.04x faster                                  |
| logging_simple          | 6.02 us                                                | 5.82 us: 1.03x faster                                 |
| regex_v8                | 22.2 ms                                                | 21.5 ms: 1.03x faster                                 |
| json                    | 4.87 ms                                                | 4.72 ms: 1.03x faster                                 |
| unpack_sequence         | 44.5 ns                                                | 43.2 ns: 1.03x faster                                 |
| pickle                  | 9.90 us                                                | 9.61 us: 1.03x faster                                 |
| python_startup          | 8.58 ms                                                | 8.33 ms: 1.03x faster                                 |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                  |
| tornado_http            | 96.5 ms                                                | 93.8 ms: 1.03x faster                                 |
| crypto_pyaes            | 75.7 ms                                                | 73.8 ms: 1.03x faster                                 |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                 |
| sympy_str               | 291 ms                                                 | 284 ms: 1.02x faster                                  |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 66.5 ms: 1.02x faster                                 |
| pyflate                 | 419 ms                                                 | 410 ms: 1.02x faster                                  |
| dulwich_log             | 64.0 ms                                                | 62.6 ms: 1.02x faster                                 |
| pickle_pure_python      | 308 us                                                 | 302 us: 1.02x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 157 ms: 1.02x faster                                  |
| spectral_norm           | 98.1 ms                                                | 96.3 ms: 1.02x faster                                 |
| richards                | 46.1 ms                                                | 45.3 ms: 1.02x faster                                 |
| html5lib                | 64.8 ms                                                | 63.8 ms: 1.02x faster                                 |
| nqueens                 | 83.8 ms                                                | 82.4 ms: 1.02x faster                                 |
| deltablue               | 3.66 ms                                                | 3.60 ms: 1.01x faster                                 |
| mako                    | 9.83 ms                                                | 9.71 ms: 1.01x faster                                 |
| chaos                   | 68.7 ms                                                | 67.8 ms: 1.01x faster                                 |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| logging_format          | 6.48 us                                                | 6.42 us: 1.01x faster                                 |
| xml_etree_process       | 53.7 ms                                                | 53.3 ms: 1.01x faster                                 |
| thrift                  | 760 us                                                 | 756 us: 1.01x faster                                  |
| scimark_fft             | 325 ms                                                 | 324 ms: 1.00x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.32 ms: 1.00x faster                                 |
| sqlite_synth            | 2.48 us                                                | 2.50 us: 1.01x slower                                 |
| pathlib                 | 18.1 ms                                                | 18.2 ms: 1.01x slower                                 |
| nbody                   | 90.0 ms                                                | 90.9 ms: 1.01x slower                                 |
| json_dumps              | 12.4 ms                                                | 12.6 ms: 1.02x slower                                 |
| python_startup_no_site  | 6.04 ms                                                | 6.17 ms: 1.02x slower                                 |
| fannkuch                | 384 ms                                                 | 394 ms: 1.03x slower                                  |
| telco                   | 6.43 ms                                                | 6.64 ms: 1.03x slower                                 |
| chameleon               | 6.38 ms                                                | 6.59 ms: 1.03x slower                                 |
| pickle_list             | 4.14 us                                                | 4.30 us: 1.04x slower                                 |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.79 ms: 1.04x slower                                 |
| Geometric mean          | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (12): scimark_lu, xml_etree_iterparse, unpickle_list, meteor_contest, scimark_sor, xml_etree_generate, regex_compile, raytrace, logging_silent, unpickle_pure_python, django_template, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
