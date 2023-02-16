
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1d81198
- commit date: 2023-02-03
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| chameleon      | 6.38 ms                                                | 6.28 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 60.0 ms: 1.08x faster                                               |
| tornado_http   | 96.5 ms                                                | 93.7 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.2 ms: 1.05x faster                                               |
| pidigits       | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| nbody          | 90.0 ms                                                | 95.8 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                               |
| regex_effbot   | 3.46 ms                                                | 3.51 ms: 1.02x slower                                               |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.43 ms: 1.31x faster                                               |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                |
| xml_etree_parse      | 160 ms                                                 | 146 ms: 1.10x faster                                                |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                               |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                |
| unpickle             | 13.3 us                                                | 12.9 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| xml_etree_process    | 53.7 ms                                                | 53.4 ms: 1.01x faster                                               |
| pickle_dict          | 31.2 us                                                | 31.3 us: 1.00x slower                                               |
| unpickle_list        | 4.99 us                                                | 5.05 us: 1.01x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 77.4 ms: 1.02x slower                                               |
| pickle_list          | 4.14 us                                                | 4.23 us: 1.02x slower                                               |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.93 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.3 ms: 1.09x faster                                               |
| genshi_text    | 21.5 ms                                                | 20.3 ms: 1.06x faster                                               |
| mako           | 9.83 ms                                                | 9.60 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.43 ms: 1.31x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.02 ms: 1.14x faster                                               |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                               |
| nqueens                 | 83.8 ms                                                | 75.7 ms: 1.11x faster                                               |
| richards                | 46.1 ms                                                | 42.0 ms: 1.10x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 146 ms: 1.10x faster                                                |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                               |
| genshi_xml              | 51.4 ms                                                | 47.3 ms: 1.09x faster                                               |
| html5lib                | 64.8 ms                                                | 60.0 ms: 1.08x faster                                               |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                |
| chaos                   | 68.7 ms                                                | 63.7 ms: 1.08x faster                                               |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                |
| coroutines              | 26.2 ms                                                | 24.3 ms: 1.08x faster                                               |
| sympy_str               | 291 ms                                                 | 271 ms: 1.07x faster                                                |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| logging_silent          | 98.0 ns                                                | 91.9 ns: 1.07x faster                                               |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                              |
| genshi_text             | 21.5 ms                                                | 20.3 ms: 1.06x faster                                               |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.06x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 671 ms: 1.05x faster                                                |
| logging_simple          | 6.02 us                                                | 5.73 us: 1.05x faster                                               |
| float                   | 76.8 ms                                                | 73.2 ms: 1.05x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                               |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                              |
| bench_thread_pool       | 817 us                                                 | 782 us: 1.04x faster                                                |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.04x faster                                               |
| fannkuch                | 384 ms                                                 | 369 ms: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| pidigits                | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                                |
| tornado_http            | 96.5 ms                                                | 93.7 ms: 1.03x faster                                               |
| coverage                | 99.3 ms                                                | 96.4 ms: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| dulwich_log             | 64.0 ms                                                | 62.3 ms: 1.03x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                               |
| logging_format          | 6.48 us                                                | 6.32 us: 1.03x faster                                               |
| unpickle                | 13.3 us                                                | 12.9 us: 1.02x faster                                               |
| mako                    | 9.83 ms                                                | 9.60 ms: 1.02x faster                                               |
| mdp                     | 2.63 sec                                               | 2.57 sec: 1.02x faster                                              |
| json                    | 4.87 ms                                                | 4.76 ms: 1.02x faster                                               |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                               |
| scimark_monte_carlo     | 68.0 ms                                                | 66.8 ms: 1.02x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                               |
| thrift                  | 760 us                                                 | 747 us: 1.02x faster                                                |
| chameleon               | 6.38 ms                                                | 6.28 ms: 1.02x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 43.9 ns: 1.01x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                |
| telco                   | 6.43 ms                                                | 6.37 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| raytrace                | 291 ms                                                 | 289 ms: 1.01x faster                                                |
| pyflate                 | 419 ms                                                 | 416 ms: 1.01x faster                                                |
| async_generators        | 356 ms                                                 | 354 ms: 1.01x faster                                                |
| xml_etree_process       | 53.7 ms                                                | 53.4 ms: 1.01x faster                                               |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.00x faster                                                |
| crypto_pyaes            | 75.7 ms                                                | 76.0 ms: 1.00x slower                                               |
| pickle_dict             | 31.2 us                                                | 31.3 us: 1.00x slower                                               |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                               |
| unpickle_list           | 4.99 us                                                | 5.05 us: 1.01x slower                                               |
| regex_effbot            | 3.46 ms                                                | 3.51 ms: 1.02x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                              |
| xml_etree_generate      | 75.9 ms                                                | 77.4 ms: 1.02x slower                                               |
| pickle_list             | 4.14 us                                                | 4.23 us: 1.02x slower                                               |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 753 ms: 1.02x slower                                                |
| sqlite_synth            | 2.48 us                                                | 2.54 us: 1.03x slower                                               |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                               |
| async_tree_memoization  | 624 ms                                                 | 647 ms: 1.04x slower                                                |
| python_startup          | 8.58 ms                                                | 8.93 ms: 1.04x slower                                               |
| generators              | 73.5 ms                                                | 77.1 ms: 1.05x slower                                               |
| gc_traversal            | 3.82 ms                                                | 4.05 ms: 1.06x slower                                               |
| nbody                   | 90.0 ms                                                | 95.8 ms: 1.07x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| dask                    | 365 ms                                                 | 494 ms: 1.35x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (6): async_tree_none, scimark_lu, django_template, djangocms, bench_mp_pool, spectral_norm
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-1d81198/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198.json: mypy
