
# Results vs. 3.11.0

- fork: brandtbucher
- ref: load_attr_managed_di
- machine: linux-x86_64
- commit hash: d5db69f
- commit date: 2023-01-17
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 250 ms: 1.03x faster                                                         |
| chameleon      | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                        |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                        |
| tornado_http   | 96.6 ms                                                | 94.0 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.8 ms: 1.05x faster                                                        |
| nbody          | 95.0 ms                                                | 92.7 ms: 1.03x faster                                                        |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 126 ms: 1.08x faster                                                         |
| regex_v8       | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                        |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                         |
| regex_effbot   | 3.36 ms                                                | 3.60 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                        |
| unpickle_pure_python | 225 us                                                 | 196 us: 1.15x faster                                                         |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                        |
| pickle_pure_python   | 304 us                                                 | 284 us: 1.07x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_list          | 4.17 us                                                | 4.08 us: 1.02x faster                                                        |
| pickle_dict          | 31.4 us                                                | 31.0 us: 1.01x faster                                                        |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.00x faster                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                        |
| unpickle_list        | 4.95 us                                                | 5.07 us: 1.02x slower                                                        |
| pickle               | 9.79 us                                                | 10.3 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.97 ms: 1.07x slower                                                        |
| python_startup_no_site | 5.96 ms                                                | 6.49 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.8 ms: 1.11x faster                                                        |
| genshi_text     | 22.1 ms                                                | 21.2 ms: 1.04x faster                                                        |
| mako            | 9.85 ms                                                | 9.56 ms: 1.03x faster                                                        |
| django_template | 32.5 ms                                                | 33.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                        |
| unpickle_pure_python    | 225 us                                                 | 196 us: 1.15x faster                                                         |
| deltablue               | 3.64 ms                                                | 3.19 ms: 1.14x faster                                                        |
| genshi_xml              | 52.1 ms                                                | 46.8 ms: 1.11x faster                                                        |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                        |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                                         |
| scimark_fft             | 329 ms                                                 | 303 ms: 1.09x faster                                                         |
| json                    | 4.95 ms                                                | 4.56 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.06 ms: 1.08x faster                                                        |
| nqueens                 | 85.0 ms                                                | 78.6 ms: 1.08x faster                                                        |
| regex_compile           | 136 ms                                                 | 126 ms: 1.08x faster                                                         |
| sympy_sum               | 166 ms                                                 | 154 ms: 1.08x faster                                                         |
| logging_simple          | 6.06 us                                                | 5.65 us: 1.07x faster                                                        |
| sympy_str               | 287 ms                                                 | 268 ms: 1.07x faster                                                         |
| richards                | 46.2 ms                                                | 43.1 ms: 1.07x faster                                                        |
| logging_silent          | 98.5 ns                                                | 92.1 ns: 1.07x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 284 us: 1.07x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| logging_format          | 6.62 us                                                | 6.20 us: 1.07x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.07x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 19.6 ms: 1.06x faster                                                        |
| chaos                   | 68.6 ms                                                | 64.7 ms: 1.06x faster                                                        |
| hexiom                  | 6.35 ms                                                | 5.99 ms: 1.06x faster                                                        |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 990 us: 1.06x faster                                                         |
| deepcopy                | 344 us                                                 | 325 us: 1.06x faster                                                         |
| regex_v8                | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                        |
| sympy_expand            | 472 ms                                                 | 449 ms: 1.05x faster                                                         |
| pycparser               | 1.17 sec                                               | 1.12 sec: 1.05x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 773 us: 1.05x faster                                                         |
| float                   | 76.3 ms                                                | 72.8 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                       |
| genshi_text             | 22.1 ms                                                | 21.2 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 65.5 ms: 1.04x faster                                                        |
| unpack_sequence         | 43.4 ns                                                | 41.7 ns: 1.04x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                         |
| coverage                | 101 ms                                                 | 97.1 ms: 1.04x faster                                                        |
| telco                   | 6.62 ms                                                | 6.41 ms: 1.03x faster                                                        |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| mako                    | 9.85 ms                                                | 9.56 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 691 ms                                                 | 671 ms: 1.03x faster                                                         |
| pyflate                 | 417 ms                                                 | 405 ms: 1.03x faster                                                         |
| 2to3                    | 257 ms                                                 | 250 ms: 1.03x faster                                                         |
| tornado_http            | 96.6 ms                                                | 94.0 ms: 1.03x faster                                                        |
| dulwich_log             | 63.9 ms                                                | 62.3 ms: 1.03x faster                                                        |
| nbody                   | 95.0 ms                                                | 92.7 ms: 1.03x faster                                                        |
| pickle_list             | 4.17 us                                                | 4.08 us: 1.02x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                                       |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                                         |
| fannkuch                | 388 ms                                                 | 382 ms: 1.02x faster                                                         |
| raytrace                | 290 ms                                                 | 286 ms: 1.02x faster                                                         |
| thrift                  | 752 us                                                 | 742 us: 1.01x faster                                                         |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.01x faster                                                        |
| crypto_pyaes            | 73.9 ms                                                | 73.0 ms: 1.01x faster                                                        |
| pickle_dict             | 31.4 us                                                | 31.0 us: 1.01x faster                                                        |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                         |
| deepcopy_reduce         | 2.97 us                                                | 2.94 us: 1.01x faster                                                        |
| chameleon               | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                        |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.00x faster                                                        |
| async_tree_cpu_io_mixed | 752 ms                                                 | 761 ms: 1.01x slower                                                         |
| xml_etree_generate      | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                        |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.01x slower                                                       |
| unpickle_list           | 4.95 us                                                | 5.07 us: 1.02x slower                                                        |
| django_template         | 32.5 ms                                                | 33.2 ms: 1.02x slower                                                        |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                         |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                                        |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                                        |
| pickle                  | 9.79 us                                                | 10.3 us: 1.05x slower                                                        |
| generators              | 72.2 ms                                                | 76.8 ms: 1.06x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.60 ms: 1.07x slower                                                        |
| python_startup          | 8.36 ms                                                | 8.97 ms: 1.07x slower                                                        |
| python_startup_no_site  | 5.96 ms                                                | 6.49 ms: 1.09x slower                                                        |
| mypy                    | 669 ms                                                 | 806 ms: 1.20x slower                                                         |
| go                      | 143 ms                                                 | 178 ms: 1.24x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (7): async_tree_memoization, unpickle, async_tree_none, spectral_norm, meteor_contest, xml_etree_iterparse, bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-d5db69f/bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
