
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 32ac98e
- commit date: 2022-08-13
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.30 ms: 1.01x faster                                  |
| html5lib       | 64.8 ms                                                | 62.9 ms: 1.03x faster                                  |
| tornado_http   | 96.5 ms                                                | 91.6 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.6 ms: 1.06x faster                                  |
| nbody          | 90.0 ms                                                | 91.3 ms: 1.01x slower                                  |
| pidigits       | 197 ms                                                 | 201 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| regex_v8       | 22.2 ms                                                | 20.9 ms: 1.06x faster                                  |
| regex_effbot   | 3.46 ms                                                | 3.42 ms: 1.01x faster                                  |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.67 ms: 1.28x faster                                  |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                   |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                   |
| xml_etree_process    | 53.7 ms                                                | 51.3 ms: 1.04x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 155 ms: 1.04x faster                                   |
| xml_etree_generate   | 75.9 ms                                                | 74.3 ms: 1.02x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                  |
| pickle_dict          | 31.2 us                                                | 31.4 us: 1.01x slower                                  |
| pickle_list          | 4.14 us                                                | 4.25 us: 1.03x slower                                  |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.17 ms: 1.05x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.04 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.21 ms: 1.07x faster                                  |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.67 ms: 1.28x faster                                  |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                  |
| pycparser               | 1.19 sec                                               | 1.05 sec: 1.13x faster                                 |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.15 ms: 1.11x faster                                  |
| logging_silent          | 98.0 ns                                                | 89.6 ns: 1.09x faster                                  |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                   |
| mako                    | 9.83 ms                                                | 9.21 ms: 1.07x faster                                  |
| regex_v8                | 22.2 ms                                                | 20.9 ms: 1.06x faster                                  |
| hexiom                  | 6.34 ms                                                | 5.97 ms: 1.06x faster                                  |
| float                   | 76.8 ms                                                | 72.6 ms: 1.06x faster                                  |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                   |
| pyflate                 | 419 ms                                                 | 397 ms: 1.05x faster                                   |
| tornado_http            | 96.5 ms                                                | 91.6 ms: 1.05x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.7 ms: 1.05x faster                                  |
| python_startup          | 8.58 ms                                                | 8.17 ms: 1.05x faster                                  |
| sympy_str               | 291 ms                                                 | 278 ms: 1.05x faster                                   |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 51.3 ms: 1.04x faster                                  |
| thrift                  | 760 us                                                 | 728 us: 1.04x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| sympy_sum               | 166 ms                                                 | 159 ms: 1.04x faster                                   |
| json                    | 4.87 ms                                                | 4.68 ms: 1.04x faster                                  |
| dulwich_log             | 64.0 ms                                                | 61.6 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| logging_simple          | 6.02 us                                                | 5.81 us: 1.04x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 155 ms: 1.04x faster                                   |
| nqueens                 | 83.8 ms                                                | 80.9 ms: 1.04x faster                                  |
| meteor_contest          | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| unpack_sequence         | 44.5 ns                                                | 43.0 ns: 1.03x faster                                  |
| scimark_sor             | 115 ms                                                 | 111 ms: 1.03x faster                                   |
| spectral_norm           | 98.1 ms                                                | 95.1 ms: 1.03x faster                                  |
| html5lib                | 64.8 ms                                                | 62.9 ms: 1.03x faster                                  |
| chaos                   | 68.7 ms                                                | 66.8 ms: 1.03x faster                                  |
| fannkuch                | 384 ms                                                 | 375 ms: 1.03x faster                                   |
| richards                | 46.1 ms                                                | 45.1 ms: 1.02x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 74.3 ms: 1.02x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.2 ms: 1.02x faster                                  |
| logging_format          | 6.48 us                                                | 6.39 us: 1.01x faster                                  |
| chameleon               | 6.38 ms                                                | 6.30 ms: 1.01x faster                                  |
| regex_effbot            | 3.46 ms                                                | 3.42 ms: 1.01x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.04 ms: 1.00x slower                                  |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                  |
| pickle_dict             | 31.2 us                                                | 31.4 us: 1.01x slower                                  |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                   |
| nbody                   | 90.0 ms                                                | 91.3 ms: 1.01x slower                                  |
| pidigits                | 197 ms                                                 | 201 ms: 1.02x slower                                   |
| pickle_list             | 4.14 us                                                | 4.25 us: 1.03x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                  |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (5): scimark_lu, unpickle, xml_etree_iterparse, raytrace, telco
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
