
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
| 2to3           | 257 ms                                                 | 258 ms: 1.00x slower                                              |
| chameleon      | 6.41 ms                                                | 6.50 ms: 1.01x slower                                             |
| docutils       | 2.60 sec                                               | 2.61 sec: 1.00x slower                                            |
| html5lib       | 63.2 ms                                                | 61.5 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.3 ms: 1.04x faster                                             |
| nbody          | 95.0 ms                                                | 95.9 ms: 1.01x slower                                             |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.01x faster                                              |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                              |
| regex_effbot   | 3.36 ms                                                | 3.53 ms: 1.05x slower                                             |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.45 ms: 1.34x faster                                             |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                             |
| pickle               | 9.79 us                                                | 10.4 us: 1.06x slower                                             |
| pickle_dict          | 31.4 us                                                | 32.4 us: 1.03x slower                                             |
| pickle_list          | 4.17 us                                                | 4.37 us: 1.05x slower                                             |
| pickle_pure_python   | 304 us                                                 | 295 us: 1.03x faster                                              |
| unpickle_pure_python | 225 us                                                 | 203 us: 1.11x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| xml_etree_iterparse  | 103 ms                                                 | 104 ms: 1.02x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                             |
| xml_etree_process    | 53.8 ms                                                | 54.1 ms: 1.01x slower                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.58 ms: 1.03x slower                                             |
| python_startup_no_site | 5.96 ms                                                | 6.11 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 34.0 ms: 1.05x slower                                             |
| genshi_text     | 22.1 ms                                                | 21.1 ms: 1.05x faster                                             |
| genshi_xml      | 52.1 ms                                                | 48.1 ms: 1.08x faster                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 258 ms: 1.00x slower                                              |
| async_generators        | 359 ms                                                 | 357 ms: 1.01x faster                                              |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed | 752 ms                                                 | 756 ms: 1.01x slower                                              |
| async_tree_memoization  | 625 ms                                                 | 659 ms: 1.05x slower                                              |
| chameleon               | 6.41 ms                                                | 6.50 ms: 1.01x slower                                             |
| bench_thread_pool       | 810 us                                                 | 792 us: 1.02x faster                                              |
| coverage                | 101 ms                                                 | 97.5 ms: 1.03x faster                                             |
| crypto_pyaes            | 73.9 ms                                                | 76.8 ms: 1.04x slower                                             |
| deepcopy                | 344 us                                                 | 346 us: 1.01x slower                                              |
| deepcopy_reduce         | 2.97 us                                                | 3.00 us: 1.01x slower                                             |
| deepcopy_memo           | 36.4 us                                                | 35.8 us: 1.02x faster                                             |
| deltablue               | 3.64 ms                                                | 3.39 ms: 1.08x faster                                             |
| django_template         | 32.5 ms                                                | 34.0 ms: 1.05x slower                                             |
| docutils                | 2.60 sec                                               | 2.61 sec: 1.00x slower                                            |
| dulwich_log             | 63.9 ms                                                | 63.6 ms: 1.01x faster                                             |
| fannkuch                | 388 ms                                                 | 379 ms: 1.02x faster                                              |
| float                   | 76.3 ms                                                | 73.3 ms: 1.04x faster                                             |
| generators              | 72.2 ms                                                | 76.3 ms: 1.06x slower                                             |
| genshi_text             | 22.1 ms                                                | 21.1 ms: 1.05x faster                                             |
| genshi_xml              | 52.1 ms                                                | 48.1 ms: 1.08x faster                                             |
| go                      | 143 ms                                                 | 140 ms: 1.02x faster                                              |
| hexiom                  | 6.35 ms                                                | 6.32 ms: 1.00x faster                                             |
| html5lib                | 63.2 ms                                                | 61.5 ms: 1.03x faster                                             |
| json                    | 4.95 ms                                                | 4.71 ms: 1.05x faster                                             |
| json_dumps              | 12.7 ms                                                | 9.45 ms: 1.34x faster                                             |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                             |
| logging_format          | 6.62 us                                                | 6.51 us: 1.02x faster                                             |
| logging_simple          | 6.06 us                                                | 5.90 us: 1.03x faster                                             |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                            |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.01x faster                                              |
| mypy                    | 669 ms                                                 | 858 ms: 1.28x slower                                              |
| nbody                   | 95.0 ms                                                | 95.9 ms: 1.01x slower                                             |
| nqueens                 | 85.0 ms                                                | 83.5 ms: 1.02x faster                                             |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                             |
| pickle                  | 9.79 us                                                | 10.4 us: 1.06x slower                                             |
| pickle_dict             | 31.4 us                                                | 32.4 us: 1.03x slower                                             |
| pickle_list             | 4.17 us                                                | 4.37 us: 1.05x slower                                             |
| pickle_pure_python      | 304 us                                                 | 295 us: 1.03x faster                                              |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                              |
| pprint_safe_repr        | 691 ms                                                 | 704 ms: 1.02x slower                                              |
| pprint_pformat          | 1.44 sec                                               | 1.42 sec: 1.01x faster                                            |
| pycparser               | 1.17 sec                                               | 1.16 sec: 1.01x faster                                            |
| pyflate                 | 417 ms                                                 | 408 ms: 1.02x faster                                              |
| python_startup          | 8.36 ms                                                | 8.58 ms: 1.03x slower                                             |
| python_startup_no_site  | 5.96 ms                                                | 6.11 ms: 1.02x slower                                             |
| raytrace                | 290 ms                                                 | 296 ms: 1.02x slower                                              |
| regex_compile           | 136 ms                                                 | 134 ms: 1.01x faster                                              |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                              |
| regex_effbot            | 3.36 ms                                                | 3.53 ms: 1.05x slower                                             |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                             |
| richards                | 46.2 ms                                                | 43.8 ms: 1.05x faster                                             |
| scimark_fft             | 329 ms                                                 | 315 ms: 1.04x faster                                              |
| scimark_lu              | 107 ms                                                 | 112 ms: 1.04x slower                                              |
| scimark_monte_carlo     | 68.3 ms                                                | 64.9 ms: 1.05x faster                                             |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.05 ms: 1.09x faster                                             |
| spectral_norm           | 99.9 ms                                                | 96.4 ms: 1.04x faster                                             |
| sqlglot_parse           | 1.37 ms                                                | 1.45 ms: 1.06x slower                                             |
| sqlglot_transpile       | 1.66 ms                                                | 1.76 ms: 1.06x slower                                             |
| sqlglot_optimize        | 53.0 ms                                                | 52.6 ms: 1.01x faster                                             |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                              |
| sqlite_synth            | 2.49 us                                                | 2.60 us: 1.04x slower                                             |
| sympy_expand            | 472 ms                                                 | 474 ms: 1.00x slower                                              |
| sympy_integrate         | 20.9 ms                                                | 22.1 ms: 1.06x slower                                             |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.01x slower                                              |
| sympy_str               | 287 ms                                                 | 291 ms: 1.01x slower                                              |
| telco                   | 6.62 ms                                                | 6.38 ms: 1.04x faster                                             |
| thrift                  | 752 us                                                 | 758 us: 1.01x slower                                              |
| unpack_sequence         | 43.4 ns                                                | 42.1 ns: 1.03x faster                                             |
| unpickle_pure_python    | 225 us                                                 | 203 us: 1.11x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| xml_etree_iterparse     | 103 ms                                                 | 104 ms: 1.02x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                             |
| xml_etree_process       | 53.8 ms                                                | 54.1 ms: 1.01x slower                                             |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (8): async_tree_io, chaos, bench_mp_pool, coroutines, logging_silent, mako, unpickle, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
