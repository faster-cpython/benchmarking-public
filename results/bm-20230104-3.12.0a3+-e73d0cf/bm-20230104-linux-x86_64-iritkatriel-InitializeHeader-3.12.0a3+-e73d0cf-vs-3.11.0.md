
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: e73d0cf
- commit date: 2023-01-04
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                    |
| chameleon      | 6.38 ms                                                | 6.17 ms: 1.03x faster                                                   |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                  |
| html5lib       | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.7 ms: 1.07x faster                                                   |
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                    |
| nbody          | 90.0 ms                                                | 92.8 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                    |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                   |
| regex_effbot   | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                   |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                   |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                    |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                                    |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                   |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                    |
| pickle_dict          | 31.2 us                                                | 30.4 us: 1.02x faster                                                   |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                                   |
| pickle_list          | 4.14 us                                                | 4.11 us: 1.01x faster                                                   |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (4): unpickle, xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.48 ms: 1.01x faster                                                   |
| python_startup_no_site | 6.04 ms                                                | 6.08 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 46.3 ms: 1.11x faster                                                   |
| genshi_text    | 21.5 ms                                                | 20.4 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                   |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                    |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.10 ms: 1.12x faster                                                   |
| genshi_xml              | 51.4 ms                                                | 46.3 ms: 1.11x faster                                                   |
| deltablue               | 3.66 ms                                                | 3.34 ms: 1.09x faster                                                   |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                                    |
| richards                | 46.1 ms                                                | 42.4 ms: 1.09x faster                                                   |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                   |
| logging_silent          | 98.0 ns                                                | 90.4 ns: 1.08x faster                                                   |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                    |
| html5lib                | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                   |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                    |
| unpack_sequence         | 44.5 ns                                                | 41.5 ns: 1.07x faster                                                   |
| pyflate                 | 419 ms                                                 | 391 ms: 1.07x faster                                                    |
| float                   | 76.8 ms                                                | 71.7 ms: 1.07x faster                                                   |
| deepcopy_memo           | 35.8 us                                                | 33.7 us: 1.06x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.4 ms: 1.06x faster                                                   |
| bench_thread_pool       | 817 us                                                 | 774 us: 1.05x faster                                                    |
| genshi_text             | 21.5 ms                                                | 20.4 ms: 1.05x faster                                                   |
| pprint_safe_repr        | 706 ms                                                 | 674 ms: 1.05x faster                                                    |
| coroutines              | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                   |
| logging_simple          | 6.02 us                                                | 5.76 us: 1.04x faster                                                   |
| fannkuch                | 384 ms                                                 | 368 ms: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                    |
| hexiom                  | 6.34 ms                                                | 6.09 ms: 1.04x faster                                                   |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                                    |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                                   |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                    |
| nqueens                 | 83.8 ms                                                | 80.6 ms: 1.04x faster                                                   |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                    |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                                   |
| deepcopy                | 341 us                                                 | 330 us: 1.04x faster                                                    |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                                    |
| chameleon               | 6.38 ms                                                | 6.17 ms: 1.03x faster                                                   |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                  |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                    |
| dulwich_log             | 64.0 ms                                                | 62.0 ms: 1.03x faster                                                   |
| json                    | 4.87 ms                                                | 4.73 ms: 1.03x faster                                                   |
| crypto_pyaes            | 75.7 ms                                                | 73.5 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                   |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                    |
| pickle_dict             | 31.2 us                                                | 30.4 us: 1.02x faster                                                   |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                    |
| mdp                     | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                  |
| logging_format          | 6.48 us                                                | 6.35 us: 1.02x faster                                                   |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                    |
| chaos                   | 68.7 ms                                                | 67.9 ms: 1.01x faster                                                   |
| python_startup          | 8.58 ms                                                | 8.48 ms: 1.01x faster                                                   |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                    |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                                   |
| pickle_list             | 4.14 us                                                | 4.11 us: 1.01x faster                                                   |
| thrift                  | 760 us                                                 | 753 us: 1.01x faster                                                    |
| coverage                | 99.3 ms                                                | 98.7 ms: 1.01x faster                                                   |
| spectral_norm           | 98.1 ms                                                | 97.5 ms: 1.01x faster                                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.08 ms: 1.01x slower                                                   |
| meteor_contest          | 104 ms                                                 | 105 ms: 1.01x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                  |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 736 ms                                                 | 750 ms: 1.02x slower                                                    |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                   |
| nbody                   | 90.0 ms                                                | 92.8 ms: 1.03x slower                                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                   |
| regex_effbot            | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                   |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                                    |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                   |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                   |
| generators              | 73.5 ms                                                | 77.1 ms: 1.05x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (13): djangocms, async_tree_none, async_generators, unpickle, telco, xml_etree_generate, async_tree_memoization, django_template, mako, pathlib, xml_etree_process, bench_mp_pool, xml_etree_iterparse
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230104-3.12.0a3+-e73d0cf/bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf.json: mypy
