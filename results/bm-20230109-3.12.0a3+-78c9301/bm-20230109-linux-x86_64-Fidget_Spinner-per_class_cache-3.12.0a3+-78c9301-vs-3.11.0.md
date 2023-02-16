
# Results vs. 3.11.0

- fork: Fidget_Spinner
- ref: per_class_cache
- machine: linux-x86_64
- commit hash: 78c9301
- commit date: 2023-01-09
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                      |
| chameleon      | 6.38 ms                                                | 6.26 ms: 1.02x faster                                                     |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                    |
| html5lib       | 64.8 ms                                                | 60.3 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.05x faster                                                     |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                      |
| nbody          | 90.0 ms                                                | 94.9 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                      |
| regex_v8       | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                     |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                      |
| regex_effbot   | 3.46 ms                                                | 3.55 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.48 ms: 1.30x faster                                                     |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                      |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                      |
| json_loads           | 26.1 us                                                | 24.3 us: 1.07x faster                                                     |
| pickle_pure_python   | 308 us                                                 | 288 us: 1.07x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.2 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.01x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 77.1 ms: 1.02x slower                                                     |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (4): unpickle_list, pickle, pickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.48 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.04 ms                                                | 6.07 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.7 ms: 1.10x faster                                                     |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                     |
| mako            | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                     |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.48 ms: 1.30x faster                                                     |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.02 ms: 1.14x faster                                                     |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 46.7 ms: 1.10x faster                                                     |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                      |
| html5lib                | 64.8 ms                                                | 60.3 ms: 1.08x faster                                                     |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                      |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                                     |
| nqueens                 | 83.8 ms                                                | 78.4 ms: 1.07x faster                                                     |
| pickle_pure_python      | 308 us                                                 | 288 us: 1.07x faster                                                      |
| coroutines              | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                     |
| float                   | 76.8 ms                                                | 72.8 ms: 1.05x faster                                                     |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                      |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                                     |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 65.1 ms: 1.04x faster                                                     |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                     |
| logging_silent          | 98.0 ns                                                | 93.9 ns: 1.04x faster                                                     |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 786 us: 1.04x faster                                                      |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 42.9 ns: 1.04x faster                                                     |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                     |
| pickle_dict             | 31.2 us                                                | 30.2 us: 1.03x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 62.0 ms: 1.03x faster                                                     |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                                     |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                    |
| hexiom                  | 6.34 ms                                                | 6.18 ms: 1.03x faster                                                     |
| coverage                | 99.3 ms                                                | 96.9 ms: 1.02x faster                                                     |
| pyflate                 | 419 ms                                                 | 409 ms: 1.02x faster                                                      |
| fannkuch                | 384 ms                                                 | 375 ms: 1.02x faster                                                      |
| telco                   | 6.43 ms                                                | 6.28 ms: 1.02x faster                                                     |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 51.6 ms: 1.02x faster                                                     |
| scimark_fft             | 325 ms                                                 | 319 ms: 1.02x faster                                                      |
| deepcopy                | 341 us                                                 | 335 us: 1.02x faster                                                      |
| chameleon               | 6.38 ms                                                | 6.26 ms: 1.02x faster                                                     |
| chaos                   | 68.7 ms                                                | 67.5 ms: 1.02x faster                                                     |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| python_startup          | 8.58 ms                                                | 8.48 ms: 1.01x faster                                                     |
| crypto_pyaes            | 75.7 ms                                                | 75.5 ms: 1.00x faster                                                     |
| regex_v8                | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                     |
| python_startup_no_site  | 6.04 ms                                                | 6.07 ms: 1.01x slower                                                     |
| mako                    | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                     |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                     |
| mdp                     | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                    |
| thrift                  | 760 us                                                 | 765 us: 1.01x slower                                                      |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.01x slower                                                      |
| deltablue               | 3.66 ms                                                | 3.71 ms: 1.01x slower                                                     |
| pathlib                 | 18.1 ms                                                | 18.3 ms: 1.01x slower                                                     |
| xml_etree_generate      | 75.9 ms                                                | 77.1 ms: 1.02x slower                                                     |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                    |
| logging_format          | 6.48 us                                                | 6.64 us: 1.03x slower                                                     |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                      |
| regex_effbot            | 3.46 ms                                                | 3.55 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed | 736 ms                                                 | 758 ms: 1.03x slower                                                      |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                                     |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                     |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                     |
| generators              | 73.5 ms                                                | 77.4 ms: 1.05x slower                                                     |
| nbody                   | 90.0 ms                                                | 94.9 ms: 1.05x slower                                                     |
| async_tree_memoization  | 624 ms                                                 | 670 ms: 1.07x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (14): djangocms, unpickle_list, richards, logging_simple, raytrace, spectral_norm, pickle, async_generators, bench_mp_pool, pickle_list, deepcopy_reduce, scimark_lu, xml_etree_process, async_tree_none
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230109-3.12.0a3+-78c9301/bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301.json: mypy
