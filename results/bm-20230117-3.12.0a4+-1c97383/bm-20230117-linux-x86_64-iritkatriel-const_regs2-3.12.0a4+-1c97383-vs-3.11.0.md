
# Results vs. 3.11.0

- fork: iritkatriel
- ref: const_regs2
- machine: linux-x86_64
- commit hash: 1c97383
- commit date: 2023-01-17
- overall geometric mean: 1.00x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 259 ms: 1.01x slower                                               |
| chameleon      | 6.41 ms                                                | 6.47 ms: 1.01x slower                                              |
| docutils       | 2.60 sec                                               | 2.61 sec: 1.01x slower                                             |
| html5lib       | 63.2 ms                                                | 60.7 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 74.9 ms: 1.02x faster                                              |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                               |
| nbody          | 95.0 ms                                                | 96.2 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.01x faster                                               |
| regex_v8       | 22.3 ms                                                | 22.6 ms: 1.01x slower                                              |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                               |
| regex_effbot   | 3.36 ms                                                | 3.47 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.51 ms: 1.33x faster                                              |
| unpickle_pure_python | 225 us                                                 | 205 us: 1.10x faster                                               |
| json_loads           | 26.2 us                                                | 24.2 us: 1.09x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| pickle_dict          | 31.4 us                                                | 30.7 us: 1.02x faster                                              |
| pickle_pure_python   | 304 us                                                 | 299 us: 1.02x faster                                               |
| unpickle_list        | 4.95 us                                                | 4.88 us: 1.01x faster                                              |
| xml_etree_process    | 53.8 ms                                                | 54.9 ms: 1.02x slower                                              |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 78.8 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (3): pickle_list, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 6.13 ms: 1.03x slower                                              |
| python_startup         | 8.36 ms                                                | 8.60 ms: 1.03x slower                                              |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.8 ms: 1.09x faster                                              |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                              |
| django_template | 32.5 ms                                                | 34.5 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.51 ms: 1.33x faster                                              |
| unpickle_pure_python    | 225 us                                                 | 205 us: 1.10x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.8 ms: 1.09x faster                                              |
| json_loads              | 26.2 us                                                | 24.2 us: 1.09x faster                                              |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.07 ms: 1.08x faster                                              |
| nqueens                 | 85.0 ms                                                | 78.9 ms: 1.08x faster                                              |
| deltablue               | 3.64 ms                                                | 3.42 ms: 1.07x faster                                              |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                              |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| scimark_fft             | 329 ms                                                 | 315 ms: 1.04x faster                                               |
| json                    | 4.95 ms                                                | 4.74 ms: 1.04x faster                                              |
| unpack_sequence         | 43.4 ns                                                | 41.7 ns: 1.04x faster                                              |
| richards                | 46.2 ms                                                | 44.4 ms: 1.04x faster                                              |
| html5lib                | 63.2 ms                                                | 60.7 ms: 1.04x faster                                              |
| scimark_sor             | 115 ms                                                 | 111 ms: 1.04x faster                                               |
| telco                   | 6.62 ms                                                | 6.41 ms: 1.03x faster                                              |
| scimark_monte_carlo     | 68.3 ms                                                | 66.1 ms: 1.03x faster                                              |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                             |
| pickle_dict             | 31.4 us                                                | 30.7 us: 1.02x faster                                              |
| pyflate                 | 417 ms                                                 | 409 ms: 1.02x faster                                               |
| float                   | 76.3 ms                                                | 74.9 ms: 1.02x faster                                              |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                             |
| deepcopy_memo           | 36.4 us                                                | 35.8 us: 1.02x faster                                              |
| pickle_pure_python      | 304 us                                                 | 299 us: 1.02x faster                                               |
| go                      | 143 ms                                                 | 141 ms: 1.02x faster                                               |
| unpickle_list           | 4.95 us                                                | 4.88 us: 1.01x faster                                              |
| regex_compile           | 136 ms                                                 | 134 ms: 1.01x faster                                               |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.01x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.43 sec: 1.01x faster                                             |
| bench_thread_pool       | 810 us                                                 | 801 us: 1.01x faster                                               |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                               |
| logging_simple          | 6.06 us                                                | 6.01 us: 1.01x faster                                              |
| async_generators        | 359 ms                                                 | 356 ms: 1.01x faster                                               |
| logging_format          | 6.62 us                                                | 6.57 us: 1.01x faster                                              |
| hexiom                  | 6.35 ms                                                | 6.31 ms: 1.01x faster                                              |
| sympy_expand            | 472 ms                                                 | 470 ms: 1.00x faster                                               |
| chaos                   | 68.6 ms                                                | 69.0 ms: 1.00x slower                                              |
| dulwich_log             | 63.9 ms                                                | 64.3 ms: 1.01x slower                                              |
| 2to3                    | 257 ms                                                 | 259 ms: 1.01x slower                                               |
| docutils                | 2.60 sec                                               | 2.61 sec: 1.01x slower                                             |
| pathlib                 | 18.2 ms                                                | 18.3 ms: 1.01x slower                                              |
| pprint_safe_repr        | 691 ms                                                 | 697 ms: 1.01x slower                                               |
| chameleon               | 6.41 ms                                                | 6.47 ms: 1.01x slower                                              |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                               |
| sympy_str               | 287 ms                                                 | 291 ms: 1.01x slower                                               |
| nbody                   | 95.0 ms                                                | 96.2 ms: 1.01x slower                                              |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| regex_v8                | 22.3 ms                                                | 22.6 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 752 ms                                                 | 765 ms: 1.02x slower                                               |
| deepcopy                | 344 us                                                 | 350 us: 1.02x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                             |
| xml_etree_process       | 53.8 ms                                                | 54.9 ms: 1.02x slower                                              |
| crypto_pyaes            | 73.9 ms                                                | 75.9 ms: 1.03x slower                                              |
| python_startup_no_site  | 5.96 ms                                                | 6.13 ms: 1.03x slower                                              |
| scimark_lu              | 107 ms                                                 | 110 ms: 1.03x slower                                               |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                              |
| python_startup          | 8.36 ms                                                | 8.60 ms: 1.03x slower                                              |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.47 ms: 1.03x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 78.8 ms: 1.03x slower                                              |
| raytrace                | 290 ms                                                 | 301 ms: 1.04x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                              |
| deepcopy_reduce         | 2.97 us                                                | 3.12 us: 1.05x slower                                              |
| sympy_integrate         | 20.9 ms                                                | 22.1 ms: 1.06x slower                                              |
| django_template         | 32.5 ms                                                | 34.5 ms: 1.06x slower                                              |
| async_tree_memoization  | 625 ms                                                 | 667 ms: 1.07x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.78 ms: 1.07x slower                                              |
| sqlglot_parse           | 1.37 ms                                                | 1.48 ms: 1.08x slower                                              |
| generators              | 72.2 ms                                                | 79.9 ms: 1.11x slower                                              |
| mypy                    | 669 ms                                                 | 857 ms: 1.28x slower                                               |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (12): coroutines, pickle_list, sqlglot_optimize, mako, bench_mp_pool, thrift, logging_silent, xml_etree_iterparse, spectral_norm, coverage, async_tree_none, unpickle
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-1c97383/bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
