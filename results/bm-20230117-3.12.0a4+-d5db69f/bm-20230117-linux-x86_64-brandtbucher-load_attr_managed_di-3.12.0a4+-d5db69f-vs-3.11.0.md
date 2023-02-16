
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
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                         |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.09x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.0 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.05x faster                                                        |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                         |
| nbody          | 90.0 ms                                                | 92.7 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 126 ms: 1.08x faster                                                         |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                        |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                         |
| regex_effbot   | 3.46 ms                                                | 3.60 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                         |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.08x faster                                                         |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| pickle_list          | 4.14 us                                                | 4.08 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.02x faster                                                         |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.00x faster                                                        |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 77.3 ms: 1.02x slower                                                        |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                        |
| mako            | 9.83 ms                                                | 9.56 ms: 1.03x faster                                                        |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                        |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.77x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                         |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.06 ms: 1.13x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                        |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                                         |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| sympy_str               | 291 ms                                                 | 268 ms: 1.09x faster                                                         |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.09x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.08x faster                                                         |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| regex_compile           | 136 ms                                                 | 126 ms: 1.08x faster                                                         |
| scimark_fft             | 325 ms                                                 | 303 ms: 1.08x faster                                                         |
| sympy_sum               | 166 ms                                                 | 154 ms: 1.07x faster                                                         |
| richards                | 46.1 ms                                                | 43.1 ms: 1.07x faster                                                        |
| json                    | 4.87 ms                                                | 4.56 ms: 1.07x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.6 ms: 1.07x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 41.7 ns: 1.07x faster                                                        |
| nqueens                 | 83.8 ms                                                | 78.6 ms: 1.07x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.65 us: 1.06x faster                                                        |
| logging_silent          | 98.0 ns                                                | 92.1 ns: 1.06x faster                                                        |
| chaos                   | 68.7 ms                                                | 64.7 ms: 1.06x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 990 us: 1.06x faster                                                         |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                       |
| sympy_expand            | 475 ms                                                 | 449 ms: 1.06x faster                                                         |
| hexiom                  | 6.34 ms                                                | 5.99 ms: 1.06x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 773 us: 1.06x faster                                                         |
| float                   | 76.8 ms                                                | 72.8 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 671 ms: 1.05x faster                                                         |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                        |
| deepcopy                | 341 us                                                 | 325 us: 1.05x faster                                                         |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                                        |
| logging_format          | 6.48 us                                                | 6.20 us: 1.04x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 65.5 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 73.0 ms: 1.04x faster                                                        |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                         |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                         |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| pyflate                 | 419 ms                                                 | 405 ms: 1.03x faster                                                         |
| mako                    | 9.83 ms                                                | 9.56 ms: 1.03x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 62.3 ms: 1.03x faster                                                        |
| tornado_http            | 96.5 ms                                                | 94.0 ms: 1.03x faster                                                        |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                                        |
| thrift                  | 760 us                                                 | 742 us: 1.02x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                       |
| coverage                | 99.3 ms                                                | 97.1 ms: 1.02x faster                                                        |
| raytrace                | 291 ms                                                 | 286 ms: 1.02x faster                                                         |
| pickle_list             | 4.14 us                                                | 4.08 us: 1.02x faster                                                        |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.02x faster                                                         |
| async_generators        | 356 ms                                                 | 353 ms: 1.01x faster                                                         |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                        |
| fannkuch                | 384 ms                                                 | 382 ms: 1.01x faster                                                         |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.00x faster                                                        |
| gc_traversal            | 3.82 ms                                                | 3.81 ms: 1.00x faster                                                        |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                         |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 77.3 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                       |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                         |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                        |
| nbody                   | 90.0 ms                                                | 92.7 ms: 1.03x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 761 ms: 1.03x slower                                                         |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                        |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| regex_effbot            | 3.46 ms                                                | 3.60 ms: 1.04x slower                                                        |
| generators              | 73.5 ms                                                | 76.8 ms: 1.05x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                        |
| go                      | 140 ms                                                 | 178 ms: 1.27x slower                                                         |
| dask                    | 365 ms                                                 | 504 ms: 1.38x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (10): async_tree_memoization, unpickle, djangocms, telco, xml_etree_process, async_tree_none, chameleon, meteor_contest, bench_mp_pool, spectral_norm
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-d5db69f/bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f.json: mypy
