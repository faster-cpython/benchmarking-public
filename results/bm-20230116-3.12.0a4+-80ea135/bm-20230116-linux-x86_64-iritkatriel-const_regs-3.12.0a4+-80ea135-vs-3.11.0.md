
# Results vs. 3.11.0

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 80ea135
- commit date: 2023-01-16
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 259 ms: 1.00x faster                                              |
| chameleon      | 6.38 ms                                                | 6.33 ms: 1.01x faster                                             |
| docutils       | 2.60 sec                                               | 2.62 sec: 1.01x slower                                            |
| html5lib       | 64.8 ms                                                | 61.5 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.1 ms: 1.04x faster                                             |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                              |
| nbody          | 90.0 ms                                                | 96.2 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                              |
| regex_v8       | 22.2 ms                                                | 22.2 ms: 1.00x faster                                             |
| regex_effbot   | 3.46 ms                                                | 3.63 ms: 1.05x slower                                             |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                             |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                              |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                             |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                              |
| pickle_pure_python   | 308 us                                                 | 297 us: 1.04x faster                                              |
| pickle_list          | 4.14 us                                                | 4.07 us: 1.02x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| xml_etree_process    | 53.7 ms                                                | 54.5 ms: 1.02x slower                                             |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                             |
| xml_etree_generate   | 75.9 ms                                                | 78.4 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (3): unpickle, pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.57 ms: 1.00x faster                                             |
| python_startup_no_site | 6.04 ms                                                | 6.11 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.6 ms: 1.08x faster                                             |
| mako            | 9.83 ms                                                | 9.60 ms: 1.02x faster                                             |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                             |
| django_template | 32.3 ms                                                | 34.3 ms: 1.06x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                              |
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                             |
| unpickle_pure_python    | 227 us                                                 | 203 us: 1.12x faster                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.15 ms: 1.11x faster                                             |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                             |
| genshi_xml              | 51.4 ms                                                | 47.6 ms: 1.08x faster                                             |
| deltablue               | 3.66 ms                                                | 3.39 ms: 1.08x faster                                             |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                              |
| nqueens                 | 83.8 ms                                                | 79.3 ms: 1.06x faster                                             |
| html5lib                | 64.8 ms                                                | 61.5 ms: 1.05x faster                                             |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                              |
| scimark_fft             | 325 ms                                                 | 311 ms: 1.05x faster                                              |
| json                    | 4.87 ms                                                | 4.65 ms: 1.05x faster                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 65.1 ms: 1.04x faster                                             |
| scimark_sor             | 115 ms                                                 | 110 ms: 1.04x faster                                              |
| richards                | 46.1 ms                                                | 44.3 ms: 1.04x faster                                             |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                              |
| pickle_pure_python      | 308 us                                                 | 297 us: 1.04x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                            |
| float                   | 76.8 ms                                                | 74.1 ms: 1.04x faster                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.03x faster                                             |
| bench_thread_pool       | 817 us                                                 | 794 us: 1.03x faster                                              |
| mako                    | 9.83 ms                                                | 9.60 ms: 1.02x faster                                             |
| pprint_safe_repr        | 706 ms                                                 | 689 ms: 1.02x faster                                              |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.02x faster                                            |
| telco                   | 6.43 ms                                                | 6.28 ms: 1.02x faster                                             |
| logging_simple          | 6.02 us                                                | 5.89 us: 1.02x faster                                             |
| thrift                  | 760 us                                                 | 745 us: 1.02x faster                                              |
| pickle_list             | 4.14 us                                                | 4.07 us: 1.02x faster                                             |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                              |
| coverage                | 99.3 ms                                                | 97.7 ms: 1.02x faster                                             |
| mdp                     | 2.63 sec                                               | 2.59 sec: 1.02x faster                                            |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| coroutines              | 26.2 ms                                                | 25.8 ms: 1.01x faster                                             |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                             |
| chameleon               | 6.38 ms                                                | 6.33 ms: 1.01x faster                                             |
| dulwich_log             | 64.0 ms                                                | 63.5 ms: 1.01x faster                                             |
| gc_traversal            | 3.82 ms                                                | 3.80 ms: 1.01x faster                                             |
| deepcopy_memo           | 35.8 us                                                | 35.6 us: 1.01x faster                                             |
| hexiom                  | 6.34 ms                                                | 6.31 ms: 1.00x faster                                             |
| sympy_expand            | 475 ms                                                 | 473 ms: 1.00x faster                                              |
| regex_v8                | 22.2 ms                                                | 22.2 ms: 1.00x faster                                             |
| 2to3                    | 259 ms                                                 | 259 ms: 1.00x faster                                              |
| python_startup          | 8.58 ms                                                | 8.57 ms: 1.00x faster                                             |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                              |
| chaos                   | 68.7 ms                                                | 69.0 ms: 1.00x slower                                             |
| deepcopy                | 341 us                                                 | 343 us: 1.00x slower                                              |
| logging_format          | 6.48 us                                                | 6.51 us: 1.01x slower                                             |
| docutils                | 2.60 sec                                               | 2.62 sec: 1.01x slower                                            |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                              |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                              |
| deepcopy_reduce         | 3.02 us                                                | 3.05 us: 1.01x slower                                             |
| async_generators        | 356 ms                                                 | 359 ms: 1.01x slower                                              |
| python_startup_no_site  | 6.04 ms                                                | 6.11 ms: 1.01x slower                                             |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                              |
| logging_silent          | 98.0 ns                                                | 99.3 ns: 1.01x slower                                             |
| crypto_pyaes            | 75.7 ms                                                | 76.8 ms: 1.01x slower                                             |
| xml_etree_process       | 53.7 ms                                                | 54.5 ms: 1.02x slower                                             |
| raytrace                | 291 ms                                                 | 298 ms: 1.02x slower                                              |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                             |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                            |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 760 ms: 1.03x slower                                              |
| xml_etree_generate      | 75.9 ms                                                | 78.4 ms: 1.03x slower                                             |
| generators              | 73.5 ms                                                | 76.1 ms: 1.04x slower                                             |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                             |
| regex_effbot            | 3.46 ms                                                | 3.63 ms: 1.05x slower                                             |
| sympy_integrate         | 21.0 ms                                                | 22.1 ms: 1.06x slower                                             |
| django_template         | 32.3 ms                                                | 34.3 ms: 1.06x slower                                             |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                              |
| nbody                   | 90.0 ms                                                | 96.2 ms: 1.07x slower                                             |
| async_tree_memoization  | 624 ms                                                 | 668 ms: 1.07x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.77 ms: 1.07x slower                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.47 ms: 1.08x slower                                             |
| dask                    | 365 ms                                                 | 518 ms: 1.42x slower                                              |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (10): unpickle, pickle_dict, sympy_str, spectral_norm, sqlglot_optimize, djangocms, bench_mp_pool, unpack_sequence, async_tree_none, unpickle_list
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230116-3.12.0a4+-80ea135/bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135.json: mypy
