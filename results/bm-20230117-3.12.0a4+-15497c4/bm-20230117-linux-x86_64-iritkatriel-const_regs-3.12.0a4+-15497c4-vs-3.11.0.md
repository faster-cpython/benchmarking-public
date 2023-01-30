
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
| chameleon      | 6.41 ms                                                | 6.52 ms: 1.02x slower                                             |
| html5lib       | 63.2 ms                                                | 60.9 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                              |
| float          | 76.3 ms                                                | 73.5 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                              |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                             |
| regex_effbot   | 3.36 ms                                                | 3.60 ms: 1.07x slower                                             |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.59 ms: 1.32x faster                                             |
| unpickle_pure_python | 225 us                                                 | 207 us: 1.09x faster                                              |
| json_loads           | 26.2 us                                                | 24.5 us: 1.07x faster                                             |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| pickle_pure_python   | 304 us                                                 | 295 us: 1.03x faster                                              |
| pickle_list          | 4.17 us                                                | 4.06 us: 1.03x faster                                             |
| pickle_dict          | 31.4 us                                                | 30.8 us: 1.02x faster                                             |
| unpickle_list        | 4.95 us                                                | 4.92 us: 1.01x faster                                             |
| xml_etree_process    | 53.8 ms                                                | 54.7 ms: 1.02x slower                                             |
| xml_etree_generate   | 76.2 ms                                                | 78.3 ms: 1.03x slower                                             |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 6.10 ms: 1.02x slower                                             |
| python_startup         | 8.36 ms                                                | 8.59 ms: 1.03x slower                                             |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 48.4 ms: 1.08x faster                                             |
| genshi_text     | 22.1 ms                                                | 20.9 ms: 1.06x faster                                             |
| mako            | 9.85 ms                                                | 9.77 ms: 1.01x faster                                             |
| django_template | 32.5 ms                                                | 33.9 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.59 ms: 1.32x faster                                             |
| unpickle_pure_python    | 225 us                                                 | 207 us: 1.09x faster                                              |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.06 ms: 1.08x faster                                             |
| deltablue               | 3.64 ms                                                | 3.38 ms: 1.08x faster                                             |
| genshi_xml              | 52.1 ms                                                | 48.4 ms: 1.08x faster                                             |
| json_loads              | 26.2 us                                                | 24.5 us: 1.07x faster                                             |
| nqueens                 | 85.0 ms                                                | 79.9 ms: 1.06x faster                                             |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                              |
| json                    | 4.95 ms                                                | 4.67 ms: 1.06x faster                                             |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                              |
| genshi_text             | 22.1 ms                                                | 20.9 ms: 1.06x faster                                             |
| richards                | 46.2 ms                                                | 43.8 ms: 1.05x faster                                             |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                              |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                            |
| telco                   | 6.62 ms                                                | 6.35 ms: 1.04x faster                                             |
| scimark_fft             | 329 ms                                                 | 316 ms: 1.04x faster                                              |
| float                   | 76.3 ms                                                | 73.5 ms: 1.04x faster                                             |
| html5lib                | 63.2 ms                                                | 60.9 ms: 1.04x faster                                             |
| deepcopy_memo           | 36.4 us                                                | 35.2 us: 1.04x faster                                             |
| unpack_sequence         | 43.4 ns                                                | 41.9 ns: 1.04x faster                                             |
| go                      | 143 ms                                                 | 139 ms: 1.03x faster                                              |
| pickle_pure_python      | 304 us                                                 | 295 us: 1.03x faster                                              |
| pickle_list             | 4.17 us                                                | 4.06 us: 1.03x faster                                             |
| logging_simple          | 6.06 us                                                | 5.92 us: 1.02x faster                                             |
| fannkuch                | 388 ms                                                 | 380 ms: 1.02x faster                                              |
| chaos                   | 68.6 ms                                                | 67.2 ms: 1.02x faster                                             |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                            |
| spectral_norm           | 99.9 ms                                                | 97.9 ms: 1.02x faster                                             |
| pickle_dict             | 31.4 us                                                | 30.8 us: 1.02x faster                                             |
| bench_thread_pool       | 810 us                                                 | 795 us: 1.02x faster                                              |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                              |
| hexiom                  | 6.35 ms                                                | 6.25 ms: 1.02x faster                                             |
| pyflate                 | 417 ms                                                 | 411 ms: 1.02x faster                                              |
| coverage                | 101 ms                                                 | 99.1 ms: 1.01x faster                                             |
| pprint_pformat          | 1.44 sec                                               | 1.42 sec: 1.01x faster                                            |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                             |
| mako                    | 9.85 ms                                                | 9.77 ms: 1.01x faster                                             |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                              |
| unpickle_list           | 4.95 us                                                | 4.92 us: 1.01x faster                                             |
| 2to3                    | 257 ms                                                 | 258 ms: 1.00x slower                                              |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                             |
| dulwich_log             | 63.9 ms                                                | 64.1 ms: 1.00x slower                                             |
| sympy_expand            | 472 ms                                                 | 475 ms: 1.01x slower                                              |
| pprint_safe_repr        | 691 ms                                                 | 695 ms: 1.01x slower                                              |
| crypto_pyaes            | 73.9 ms                                                | 74.7 ms: 1.01x slower                                             |
| sympy_str               | 287 ms                                                 | 291 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 752 ms                                                 | 762 ms: 1.01x slower                                              |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.02x slower                                              |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                            |
| xml_etree_process       | 53.8 ms                                                | 54.7 ms: 1.02x slower                                             |
| chameleon               | 6.41 ms                                                | 6.52 ms: 1.02x slower                                             |
| deepcopy_reduce         | 2.97 us                                                | 3.02 us: 1.02x slower                                             |
| scimark_lu              | 107 ms                                                 | 110 ms: 1.02x slower                                              |
| python_startup_no_site  | 5.96 ms                                                | 6.10 ms: 1.02x slower                                             |
| meteor_contest          | 105 ms                                                 | 107 ms: 1.02x slower                                              |
| sqlglot_normalize       | 108 ms                                                 | 110 ms: 1.02x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 78.3 ms: 1.03x slower                                             |
| coroutines              | 26.1 ms                                                | 26.8 ms: 1.03x slower                                             |
| python_startup          | 8.36 ms                                                | 8.59 ms: 1.03x slower                                             |
| raytrace                | 290 ms                                                 | 301 ms: 1.03x slower                                              |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                             |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                             |
| django_template         | 32.5 ms                                                | 33.9 ms: 1.04x slower                                             |
| sympy_integrate         | 20.9 ms                                                | 22.1 ms: 1.06x slower                                             |
| sqlglot_transpile       | 1.66 ms                                                | 1.76 ms: 1.06x slower                                             |
| sqlglot_parse           | 1.37 ms                                                | 1.46 ms: 1.06x slower                                             |
| async_tree_memoization  | 625 ms                                                 | 670 ms: 1.07x slower                                              |
| regex_effbot            | 3.36 ms                                                | 3.60 ms: 1.07x slower                                             |
| generators              | 72.2 ms                                                | 77.6 ms: 1.07x slower                                             |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                              |
| mypy                    | 669 ms                                                 | 860 ms: 1.29x slower                                              |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (12): logging_silent, logging_format, scimark_monte_carlo, async_tree_none, thrift, bench_mp_pool, sqlglot_optimize, docutils, deepcopy, xml_etree_iterparse, nbody, unpickle
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
