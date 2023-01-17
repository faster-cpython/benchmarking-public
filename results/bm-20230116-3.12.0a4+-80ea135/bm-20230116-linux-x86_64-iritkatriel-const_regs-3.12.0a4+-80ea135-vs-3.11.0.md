
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
| 2to3           | 257 ms                                                 | 259 ms: 1.01x slower                                              |
| chameleon      | 6.41 ms                                                | 6.33 ms: 1.01x faster                                             |
| docutils       | 2.60 sec                                               | 2.62 sec: 1.01x slower                                            |
| html5lib       | 63.2 ms                                                | 61.5 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.3 ms                                                | 74.1 ms: 1.03x faster                                             |
| nbody          | 95.0 ms                                                | 96.2 ms: 1.01x slower                                             |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.01x faster                                              |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                              |
| regex_effbot   | 3.36 ms                                                | 3.63 ms: 1.08x slower                                             |
| regex_v8       | 22.3 ms                                                | 22.2 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.44 ms: 1.34x faster                                             |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                             |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                             |
| pickle_dict          | 31.4 us                                                | 31.1 us: 1.01x faster                                             |
| pickle_list          | 4.17 us                                                | 4.07 us: 1.03x faster                                             |
| pickle_pure_python   | 304 us                                                 | 297 us: 1.02x faster                                              |
| unpickle_list        | 4.95 us                                                | 5.00 us: 1.01x slower                                             |
| unpickle_pure_python | 225 us                                                 | 203 us: 1.11x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| xml_etree_generate   | 76.2 ms                                                | 78.4 ms: 1.03x slower                                             |
| xml_etree_process    | 53.8 ms                                                | 54.5 ms: 1.01x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.57 ms: 1.03x slower                                             |
| python_startup_no_site | 5.96 ms                                                | 6.11 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 34.3 ms: 1.06x slower                                             |
| genshi_text     | 22.1 ms                                                | 21.2 ms: 1.04x faster                                             |
| genshi_xml      | 52.1 ms                                                | 47.6 ms: 1.09x faster                                             |
| mako            | 9.85 ms                                                | 9.60 ms: 1.03x faster                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 259 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 752 ms                                                 | 760 ms: 1.01x slower                                              |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                            |
| async_tree_memoization  | 625 ms                                                 | 668 ms: 1.07x slower                                              |
| chameleon               | 6.41 ms                                                | 6.33 ms: 1.01x faster                                             |
| chaos                   | 68.6 ms                                                | 69.0 ms: 1.01x slower                                             |
| bench_thread_pool       | 810 us                                                 | 794 us: 1.02x faster                                              |
| coroutines              | 26.1 ms                                                | 25.8 ms: 1.01x faster                                             |
| coverage                | 101 ms                                                 | 97.7 ms: 1.03x faster                                             |
| crypto_pyaes            | 73.9 ms                                                | 76.8 ms: 1.04x slower                                             |
| deepcopy_reduce         | 2.97 us                                                | 3.05 us: 1.03x slower                                             |
| deepcopy_memo           | 36.4 us                                                | 35.6 us: 1.02x faster                                             |
| deltablue               | 3.64 ms                                                | 3.39 ms: 1.07x faster                                             |
| django_template         | 32.5 ms                                                | 34.3 ms: 1.06x slower                                             |
| docutils                | 2.60 sec                                               | 2.62 sec: 1.01x slower                                            |
| dulwich_log             | 63.9 ms                                                | 63.5 ms: 1.01x faster                                             |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                              |
| float                   | 76.3 ms                                                | 74.1 ms: 1.03x faster                                             |
| generators              | 72.2 ms                                                | 76.1 ms: 1.05x slower                                             |
| genshi_text             | 22.1 ms                                                | 21.2 ms: 1.04x faster                                             |
| genshi_xml              | 52.1 ms                                                | 47.6 ms: 1.09x faster                                             |
| go                      | 143 ms                                                 | 141 ms: 1.01x faster                                              |
| hexiom                  | 6.35 ms                                                | 6.31 ms: 1.01x faster                                             |
| html5lib                | 63.2 ms                                                | 61.5 ms: 1.03x faster                                             |
| json                    | 4.95 ms                                                | 4.65 ms: 1.06x faster                                             |
| json_dumps              | 12.7 ms                                                | 9.44 ms: 1.34x faster                                             |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                             |
| logging_format          | 6.62 us                                                | 6.51 us: 1.02x faster                                             |
| logging_silent          | 98.5 ns                                                | 99.3 ns: 1.01x slower                                             |
| logging_simple          | 6.06 us                                                | 5.89 us: 1.03x faster                                             |
| mako                    | 9.85 ms                                                | 9.60 ms: 1.03x faster                                             |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                            |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                              |
| mypy                    | 669 ms                                                 | 861 ms: 1.29x slower                                              |
| nbody                   | 95.0 ms                                                | 96.2 ms: 1.01x slower                                             |
| nqueens                 | 85.0 ms                                                | 79.3 ms: 1.07x faster                                             |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                             |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                             |
| pickle_dict             | 31.4 us                                                | 31.1 us: 1.01x faster                                             |
| pickle_list             | 4.17 us                                                | 4.07 us: 1.03x faster                                             |
| pickle_pure_python      | 304 us                                                 | 297 us: 1.02x faster                                              |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                              |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                            |
| pycparser               | 1.17 sec                                               | 1.16 sec: 1.01x faster                                            |
| pyflate                 | 417 ms                                                 | 402 ms: 1.04x faster                                              |
| python_startup          | 8.36 ms                                                | 8.57 ms: 1.03x slower                                             |
| python_startup_no_site  | 5.96 ms                                                | 6.11 ms: 1.02x slower                                             |
| raytrace                | 290 ms                                                 | 298 ms: 1.03x slower                                              |
| regex_compile           | 136 ms                                                 | 134 ms: 1.01x faster                                              |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                              |
| regex_effbot            | 3.36 ms                                                | 3.63 ms: 1.08x slower                                             |
| regex_v8                | 22.3 ms                                                | 22.2 ms: 1.00x faster                                             |
| richards                | 46.2 ms                                                | 44.3 ms: 1.04x faster                                             |
| scimark_fft             | 329 ms                                                 | 311 ms: 1.06x faster                                              |
| scimark_lu              | 107 ms                                                 | 111 ms: 1.04x slower                                              |
| scimark_monte_carlo     | 68.3 ms                                                | 65.1 ms: 1.05x faster                                             |
| scimark_sor             | 115 ms                                                 | 110 ms: 1.04x faster                                              |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.15 ms: 1.06x faster                                             |
| spectral_norm           | 99.9 ms                                                | 98.1 ms: 1.02x faster                                             |
| sqlglot_parse           | 1.37 ms                                                | 1.47 ms: 1.07x slower                                             |
| sqlglot_transpile       | 1.66 ms                                                | 1.77 ms: 1.07x slower                                             |
| sqlglot_optimize        | 53.0 ms                                                | 52.7 ms: 1.01x faster                                             |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                              |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                             |
| sympy_integrate         | 20.9 ms                                                | 22.1 ms: 1.06x slower                                             |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                              |
| sympy_str               | 287 ms                                                 | 291 ms: 1.01x slower                                              |
| telco                   | 6.62 ms                                                | 6.28 ms: 1.05x faster                                             |
| thrift                  | 752 us                                                 | 745 us: 1.01x faster                                              |
| unpack_sequence         | 43.4 ns                                                | 44.5 ns: 1.03x slower                                             |
| unpickle_list           | 4.95 us                                                | 5.00 us: 1.01x slower                                             |
| unpickle_pure_python    | 225 us                                                 | 203 us: 1.11x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| xml_etree_generate      | 76.2 ms                                                | 78.4 ms: 1.03x slower                                             |
| xml_etree_process       | 53.8 ms                                                | 54.5 ms: 1.01x slower                                             |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (8): async_generators, async_tree_none, bench_mp_pool, deepcopy, pprint_safe_repr, sympy_expand, unpickle, xml_etree_iterparse
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230116-3.12.0a4+-80ea135/bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
