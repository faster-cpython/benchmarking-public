
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.06x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| chameleon      | 6.38 ms                                                | 7.44 ms: 1.17x slower                                 |
| html5lib       | 64.8 ms                                                | 68.5 ms: 1.06x slower                                 |
| tornado_http   | 96.5 ms                                                | 108 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 197 ms                                                 | 198 ms: 1.01x slower                                  |
| float          | 76.8 ms                                                | 79.2 ms: 1.03x slower                                 |
| nbody          | 90.0 ms                                                | 96.1 ms: 1.07x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.21 ms: 1.08x faster                                 |
| regex_compile  | 136 ms                                                 | 139 ms: 1.02x slower                                  |
| regex_dna      | 203 ms                                                 | 212 ms: 1.04x slower                                  |
| regex_v8       | 22.2 ms                                                | 24.5 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 27.7 us: 1.13x faster                                 |
| xml_etree_parse      | 160 ms                                                 | 156 ms: 1.03x faster                                  |
| json_loads           | 26.1 us                                                | 25.6 us: 1.02x faster                                 |
| pickle               | 9.90 us                                                | 9.95 us: 1.01x slower                                 |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                  |
| json_dumps           | 12.4 ms                                                | 12.6 ms: 1.02x slower                                 |
| unpickle_list        | 4.99 us                                                | 5.21 us: 1.04x slower                                 |
| xml_etree_generate   | 75.9 ms                                                | 80.8 ms: 1.07x slower                                 |
| xml_etree_process    | 53.7 ms                                                | 57.8 ms: 1.08x slower                                 |
| unpickle             | 13.3 us                                                | 14.6 us: 1.10x slower                                 |
| unpickle_pure_python | 227 us                                                 | 251 us: 1.11x slower                                  |
| pickle_pure_python   | 308 us                                                 | 347 us: 1.13x slower                                  |
| pickle_list          | 4.14 us                                                | 4.68 us: 1.13x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.00 ms: 1.07x faster                                 |
| python_startup_no_site | 6.04 ms                                                | 5.78 ms: 1.04x faster                                 |
| Geometric mean         | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.3 ms                                                | 36.5 ms: 1.13x slower                                 |
| mako            | 9.83 ms                                                | 11.9 ms: 1.21x slower                                 |
| Geometric mean  | (ref)                                                  | 1.17x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 31.2 us                                                | 27.7 us: 1.13x faster                                 |
| regex_effbot            | 3.46 ms                                                | 3.21 ms: 1.08x faster                                 |
| python_startup          | 8.58 ms                                                | 8.00 ms: 1.07x faster                                 |
| python_startup_no_site  | 6.04 ms                                                | 5.78 ms: 1.04x faster                                 |
| xml_etree_parse         | 160 ms                                                 | 156 ms: 1.03x faster                                  |
| json_loads              | 26.1 us                                                | 25.6 us: 1.02x faster                                 |
| logging_simple          | 6.02 us                                                | 5.97 us: 1.01x faster                                 |
| json                    | 4.87 ms                                                | 4.83 ms: 1.01x faster                                 |
| pickle                  | 9.90 us                                                | 9.95 us: 1.01x slower                                 |
| pidigits                | 197 ms                                                 | 198 ms: 1.01x slower                                  |
| nqueens                 | 83.8 ms                                                | 84.6 ms: 1.01x slower                                 |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                  |
| 2to3                    | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| regex_compile           | 136 ms                                                 | 139 ms: 1.02x slower                                  |
| json_dumps              | 12.4 ms                                                | 12.6 ms: 1.02x slower                                 |
| telco                   | 6.43 ms                                                | 6.56 ms: 1.02x slower                                 |
| scimark_fft             | 325 ms                                                 | 332 ms: 1.02x slower                                  |
| float                   | 76.8 ms                                                | 79.2 ms: 1.03x slower                                 |
| scimark_lu              | 108 ms                                                 | 112 ms: 1.04x slower                                  |
| sympy_sum               | 166 ms                                                 | 172 ms: 1.04x slower                                  |
| sympy_integrate         | 21.0 ms                                                | 21.7 ms: 1.04x slower                                 |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.77 ms: 1.04x slower                                 |
| regex_dna               | 203 ms                                                 | 212 ms: 1.04x slower                                  |
| pycparser               | 1.19 sec                                               | 1.24 sec: 1.04x slower                                |
| unpickle_list           | 4.99 us                                                | 5.21 us: 1.04x slower                                 |
| dulwich_log             | 64.0 ms                                                | 67.2 ms: 1.05x slower                                 |
| spectral_norm           | 98.1 ms                                                | 104 ms: 1.05x slower                                  |
| html5lib                | 64.8 ms                                                | 68.5 ms: 1.06x slower                                 |
| sympy_str               | 291 ms                                                 | 308 ms: 1.06x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 80.8 ms: 1.07x slower                                 |
| nbody                   | 90.0 ms                                                | 96.1 ms: 1.07x slower                                 |
| hexiom                  | 6.34 ms                                                | 6.77 ms: 1.07x slower                                 |
| sympy_expand            | 475 ms                                                 | 509 ms: 1.07x slower                                  |
| thrift                  | 760 us                                                 | 814 us: 1.07x slower                                  |
| pathlib                 | 18.1 ms                                                | 19.4 ms: 1.08x slower                                 |
| chaos                   | 68.7 ms                                                | 73.9 ms: 1.08x slower                                 |
| xml_etree_process       | 53.7 ms                                                | 57.8 ms: 1.08x slower                                 |
| scimark_monte_carlo     | 68.0 ms                                                | 74.0 ms: 1.09x slower                                 |
| unpickle                | 13.3 us                                                | 14.6 us: 1.10x slower                                 |
| regex_v8                | 22.2 ms                                                | 24.5 ms: 1.10x slower                                 |
| sqlite_synth            | 2.48 us                                                | 2.74 us: 1.10x slower                                 |
| unpack_sequence         | 44.5 ns                                                | 49.2 ns: 1.11x slower                                 |
| unpickle_pure_python    | 227 us                                                 | 251 us: 1.11x slower                                  |
| tornado_http            | 96.5 ms                                                | 108 ms: 1.12x slower                                  |
| go                      | 140 ms                                                 | 158 ms: 1.12x slower                                  |
| logging_silent          | 98.0 ns                                                | 110 ns: 1.13x slower                                  |
| pickle_pure_python      | 308 us                                                 | 347 us: 1.13x slower                                  |
| pickle_list             | 4.14 us                                                | 4.68 us: 1.13x slower                                 |
| django_template         | 32.3 ms                                                | 36.5 ms: 1.13x slower                                 |
| scimark_sor             | 115 ms                                                 | 130 ms: 1.13x slower                                  |
| pyflate                 | 419 ms                                                 | 477 ms: 1.14x slower                                  |
| raytrace                | 291 ms                                                 | 333 ms: 1.14x slower                                  |
| crypto_pyaes            | 75.7 ms                                                | 88.1 ms: 1.16x slower                                 |
| chameleon               | 6.38 ms                                                | 7.44 ms: 1.17x slower                                 |
| richards                | 46.1 ms                                                | 54.5 ms: 1.18x slower                                 |
| mako                    | 9.83 ms                                                | 11.9 ms: 1.21x slower                                 |
| deltablue               | 3.66 ms                                                | 4.54 ms: 1.24x slower                                 |
| Geometric mean          | (ref)                                                  | 1.06x slower                                          |

Benchmark hidden because not significant (3): meteor_contest, logging_format, fannkuch
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
