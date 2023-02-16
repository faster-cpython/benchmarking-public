
# Results vs. 3.11.0

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 15497c4
- commit date: 2023-01-17
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 258 ms: 1.01x faster                                              |
| chameleon      | 6.38 ms                                                | 6.52 ms: 1.02x slower                                             |
| html5lib       | 64.8 ms                                                | 60.9 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.5 ms: 1.04x faster                                             |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                              |
| nbody          | 90.0 ms                                                | 95.6 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                              |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                             |
| regex_effbot   | 3.46 ms                                                | 3.60 ms: 1.04x slower                                             |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.59 ms: 1.29x faster                                             |
| unpickle_pure_python | 227 us                                                 | 207 us: 1.10x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.07x faster                                              |
| json_loads           | 26.1 us                                                | 24.5 us: 1.06x faster                                             |
| pickle_pure_python   | 308 us                                                 | 295 us: 1.04x faster                                              |
| pickle_list          | 4.14 us                                                | 4.06 us: 1.02x faster                                             |
| unpickle_list        | 4.99 us                                                | 4.92 us: 1.01x faster                                             |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| xml_etree_process    | 53.7 ms                                                | 54.7 ms: 1.02x slower                                             |
| xml_etree_generate   | 75.9 ms                                                | 78.3 ms: 1.03x slower                                             |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.59 ms: 1.00x slower                                             |
| python_startup_no_site | 6.04 ms                                                | 6.10 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.4 ms: 1.06x faster                                             |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                             |
| mako            | 9.83 ms                                                | 9.77 ms: 1.01x faster                                             |
| django_template | 32.3 ms                                                | 33.9 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                              |
| json_dumps              | 12.4 ms                                                | 9.59 ms: 1.29x faster                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.06 ms: 1.13x faster                                             |
| unpickle_pure_python    | 227 us                                                 | 207 us: 1.10x faster                                              |
| deltablue               | 3.66 ms                                                | 3.38 ms: 1.08x faster                                             |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.07x faster                                              |
| html5lib                | 64.8 ms                                                | 60.9 ms: 1.06x faster                                             |
| json_loads              | 26.1 us                                                | 24.5 us: 1.06x faster                                             |
| genshi_xml              | 51.4 ms                                                | 48.4 ms: 1.06x faster                                             |
| unpack_sequence         | 44.5 ns                                                | 41.9 ns: 1.06x faster                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.43 ms: 1.06x faster                                             |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                              |
| richards                | 46.1 ms                                                | 43.8 ms: 1.05x faster                                             |
| mdp                     | 2.63 sec                                               | 2.50 sec: 1.05x faster                                            |
| nqueens                 | 83.8 ms                                                | 79.9 ms: 1.05x faster                                             |
| float                   | 76.8 ms                                                | 73.5 ms: 1.04x faster                                             |
| pickle_pure_python      | 308 us                                                 | 295 us: 1.04x faster                                              |
| json                    | 4.87 ms                                                | 4.67 ms: 1.04x faster                                             |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                              |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                            |
| scimark_fft             | 325 ms                                                 | 316 ms: 1.03x faster                                              |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                             |
| bench_thread_pool       | 817 us                                                 | 795 us: 1.03x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                            |
| chaos                   | 68.7 ms                                                | 67.2 ms: 1.02x faster                                             |
| pickle_list             | 4.14 us                                                | 4.06 us: 1.02x faster                                             |
| pyflate                 | 419 ms                                                 | 411 ms: 1.02x faster                                              |
| deepcopy_memo           | 35.8 us                                                | 35.2 us: 1.02x faster                                             |
| logging_simple          | 6.02 us                                                | 5.92 us: 1.02x faster                                             |
| pprint_safe_repr        | 706 ms                                                 | 695 ms: 1.02x faster                                              |
| hexiom                  | 6.34 ms                                                | 6.25 ms: 1.01x faster                                             |
| crypto_pyaes            | 75.7 ms                                                | 74.7 ms: 1.01x faster                                             |
| unpickle_list           | 4.99 us                                                | 4.92 us: 1.01x faster                                             |
| telco                   | 6.43 ms                                                | 6.35 ms: 1.01x faster                                             |
| fannkuch                | 384 ms                                                 | 380 ms: 1.01x faster                                              |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                             |
| thrift                  | 760 us                                                 | 751 us: 1.01x faster                                              |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                              |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| async_generators        | 356 ms                                                 | 353 ms: 1.01x faster                                              |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                              |
| 2to3                    | 259 ms                                                 | 258 ms: 1.01x faster                                              |
| mako                    | 9.83 ms                                                | 9.77 ms: 1.01x faster                                             |
| python_startup          | 8.58 ms                                                | 8.59 ms: 1.00x slower                                             |
| dulwich_log             | 64.0 ms                                                | 64.1 ms: 1.00x slower                                             |
| sqlglot_optimize        | 52.7 ms                                                | 53.0 ms: 1.01x slower                                             |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                             |
| deepcopy                | 341 us                                                 | 345 us: 1.01x slower                                              |
| python_startup_no_site  | 6.04 ms                                                | 6.10 ms: 1.01x slower                                             |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.02x slower                                              |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                              |
| logging_format          | 6.48 us                                                | 6.59 us: 1.02x slower                                             |
| xml_etree_process       | 53.7 ms                                                | 54.7 ms: 1.02x slower                                             |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                            |
| chameleon               | 6.38 ms                                                | 6.52 ms: 1.02x slower                                             |
| coroutines              | 26.2 ms                                                | 26.8 ms: 1.02x slower                                             |
| sqlglot_normalize       | 108 ms                                                 | 110 ms: 1.03x slower                                              |
| meteor_contest          | 104 ms                                                 | 107 ms: 1.03x slower                                              |
| raytrace                | 291 ms                                                 | 301 ms: 1.03x slower                                              |
| xml_etree_generate      | 75.9 ms                                                | 78.3 ms: 1.03x slower                                             |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                             |
| async_tree_cpu_io_mixed | 736 ms                                                 | 762 ms: 1.04x slower                                              |
| regex_effbot            | 3.46 ms                                                | 3.60 ms: 1.04x slower                                             |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                             |
| django_template         | 32.3 ms                                                | 33.9 ms: 1.05x slower                                             |
| sympy_integrate         | 21.0 ms                                                | 22.1 ms: 1.05x slower                                             |
| generators              | 73.5 ms                                                | 77.6 ms: 1.06x slower                                             |
| nbody                   | 90.0 ms                                                | 95.6 ms: 1.06x slower                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.76 ms: 1.07x slower                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.46 ms: 1.07x slower                                             |
| async_tree_memoization  | 624 ms                                                 | 670 ms: 1.07x slower                                              |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                              |
| gc_traversal            | 3.82 ms                                                | 4.15 ms: 1.09x slower                                             |
| dask                    | 365 ms                                                 | 516 ms: 1.41x slower                                              |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (13): pathlib, logging_silent, spectral_norm, coverage, docutils, sympy_expand, sympy_str, bench_mp_pool, deepcopy_reduce, scimark_monte_carlo, async_tree_none, unpickle, djangocms
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: mypy
