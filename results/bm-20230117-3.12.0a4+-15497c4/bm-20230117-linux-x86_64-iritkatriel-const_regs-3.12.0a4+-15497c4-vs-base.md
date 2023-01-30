
# Results vs. base

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 15497c4
- commit date: 2023-01-17
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 258 ms: 1.02x slower                                              |
| chameleon      | 6.31 ms                                                                | 6.52 ms: 1.03x slower                                             |
| docutils       | 2.50 sec                                                               | 2.60 sec: 1.04x slower                                            |
| html5lib       | 59.5 ms                                                                | 60.9 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 190 ms: 1.01x faster                                              |
| float          | 72.1 ms                                                                | 73.5 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                                | 22.4 ms: 1.02x slower                                             |
| regex_dna      | 211 ms                                                                 | 219 ms: 1.04x slower                                              |
| regex_compile  | 129 ms                                                                 | 135 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_iterparse  | 109 ms                                                                 | 103 ms: 1.05x faster                                              |
| unpickle_list        | 4.98 us                                                                | 4.92 us: 1.01x faster                                             |
| pickle_dict          | 30.4 us                                                                | 30.8 us: 1.01x slower                                             |
| pickle               | 10.1 us                                                                | 10.2 us: 1.02x slower                                             |
| xml_etree_process    | 53.8 ms                                                                | 54.7 ms: 1.02x slower                                             |
| xml_etree_generate   | 76.8 ms                                                                | 78.3 ms: 1.02x slower                                             |
| json_dumps           | 9.37 ms                                                                | 9.59 ms: 1.02x slower                                             |
| json_loads           | 23.8 us                                                                | 24.5 us: 1.03x slower                                             |
| unpickle             | 12.9 us                                                                | 13.3 us: 1.04x slower                                             |
| unpickle_pure_python | 200 us                                                                 | 207 us: 1.04x slower                                              |
| pickle_pure_python   | 281 us                                                                 | 295 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.06 ms                                                                | 6.10 ms: 1.01x slower                                             |
| python_startup         | 8.50 ms                                                                | 8.59 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 20.2 ms                                                                | 20.9 ms: 1.04x slower                                             |
| genshi_xml      | 46.5 ms                                                                | 48.4 ms: 1.04x slower                                             |
| django_template | 32.3 ms                                                                | 33.9 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_iterparse     | 109 ms                                                                 | 103 ms: 1.05x faster                                              |
| unpack_sequence         | 43.8 ns                                                                | 41.9 ns: 1.05x faster                                             |
| generators              | 79.3 ms                                                                | 77.6 ms: 1.02x faster                                             |
| pidigits                | 192 ms                                                                 | 190 ms: 1.01x faster                                              |
| create_gc_cycles        | 1.45 ms                                                                | 1.43 ms: 1.01x faster                                             |
| unpickle_list           | 4.98 us                                                                | 4.92 us: 1.01x faster                                             |
| async_generators        | 357 ms                                                                 | 353 ms: 1.01x faster                                              |
| crypto_pyaes            | 75.1 ms                                                                | 74.7 ms: 1.01x faster                                             |
| asyncio_tcp             | 503 ms                                                                 | 504 ms: 1.00x slower                                              |
| nqueens                 | 79.6 ms                                                                | 79.9 ms: 1.00x slower                                             |
| sqlite_synth            | 2.57 us                                                                | 2.59 us: 1.01x slower                                             |
| python_startup_no_site  | 6.06 ms                                                                | 6.10 ms: 1.01x slower                                             |
| chaos                   | 66.7 ms                                                                | 67.2 ms: 1.01x slower                                             |
| pathlib                 | 17.8 ms                                                                | 18.0 ms: 1.01x slower                                             |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                            |
| python_startup          | 8.50 ms                                                                | 8.59 ms: 1.01x slower                                             |
| scimark_fft             | 312 ms                                                                 | 316 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 753 ms                                                                 | 762 ms: 1.01x slower                                              |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                            |
| pickle_dict             | 30.4 us                                                                | 30.8 us: 1.01x slower                                             |
| spectral_norm           | 96.4 ms                                                                | 97.9 ms: 1.02x slower                                             |
| pickle                  | 10.1 us                                                                | 10.2 us: 1.02x slower                                             |
| bench_thread_pool       | 782 us                                                                 | 795 us: 1.02x slower                                              |
| xml_etree_process       | 53.8 ms                                                                | 54.7 ms: 1.02x slower                                             |
| 2to3                    | 253 ms                                                                 | 258 ms: 1.02x slower                                              |
| regex_v8                | 22.0 ms                                                                | 22.4 ms: 1.02x slower                                             |
| float                   | 72.1 ms                                                                | 73.5 ms: 1.02x slower                                             |
| xml_etree_generate      | 76.8 ms                                                                | 78.3 ms: 1.02x slower                                             |
| mdp                     | 2.44 sec                                                               | 2.50 sec: 1.02x slower                                            |
| scimark_lu              | 107 ms                                                                 | 110 ms: 1.02x slower                                              |
| html5lib                | 59.5 ms                                                                | 60.9 ms: 1.02x slower                                             |
| json_dumps              | 9.37 ms                                                                | 9.59 ms: 1.02x slower                                             |
| scimark_sor             | 106 ms                                                                 | 109 ms: 1.02x slower                                              |
| go                      | 136 ms                                                                 | 139 ms: 1.03x slower                                              |
| json_loads              | 23.8 us                                                                | 24.5 us: 1.03x slower                                             |
| hexiom                  | 6.07 ms                                                                | 6.25 ms: 1.03x slower                                             |
| logging_simple          | 5.75 us                                                                | 5.92 us: 1.03x slower                                             |
| sqlglot_parse           | 1.41 ms                                                                | 1.46 ms: 1.03x slower                                             |
| sqlglot_transpile       | 1.71 ms                                                                | 1.76 ms: 1.03x slower                                             |
| pprint_pformat          | 1.38 sec                                                               | 1.42 sec: 1.03x slower                                            |
| dulwich_log             | 62.0 ms                                                                | 64.1 ms: 1.03x slower                                             |
| chameleon               | 6.31 ms                                                                | 6.52 ms: 1.03x slower                                             |
| deepcopy_memo           | 34.0 us                                                                | 35.2 us: 1.03x slower                                             |
| genshi_text             | 20.2 ms                                                                | 20.9 ms: 1.04x slower                                             |
| unpickle                | 12.9 us                                                                | 13.3 us: 1.04x slower                                             |
| sympy_sum               | 162 ms                                                                 | 168 ms: 1.04x slower                                              |
| unpickle_pure_python    | 200 us                                                                 | 207 us: 1.04x slower                                              |
| docutils                | 2.50 sec                                                               | 2.60 sec: 1.04x slower                                            |
| logging_silent          | 93.9 ns                                                                | 97.7 ns: 1.04x slower                                             |
| sqlglot_optimize        | 51.0 ms                                                                | 53.0 ms: 1.04x slower                                             |
| fannkuch                | 365 ms                                                                 | 380 ms: 1.04x slower                                              |
| sympy_str               | 280 ms                                                                 | 291 ms: 1.04x slower                                              |
| meteor_contest          | 103 ms                                                                 | 107 ms: 1.04x slower                                              |
| genshi_xml              | 46.5 ms                                                                | 48.4 ms: 1.04x slower                                             |
| deltablue               | 3.24 ms                                                                | 3.38 ms: 1.04x slower                                             |
| deepcopy                | 331 us                                                                 | 345 us: 1.04x slower                                              |
| regex_dna               | 211 ms                                                                 | 219 ms: 1.04x slower                                              |
| regex_compile           | 129 ms                                                                 | 135 ms: 1.04x slower                                              |
| pprint_safe_repr        | 666 ms                                                                 | 695 ms: 1.04x slower                                              |
| pyflate                 | 393 ms                                                                 | 411 ms: 1.04x slower                                              |
| richards                | 41.9 ms                                                                | 43.8 ms: 1.05x slower                                             |
| sympy_expand            | 453 ms                                                                 | 475 ms: 1.05x slower                                              |
| django_template         | 32.3 ms                                                                | 33.9 ms: 1.05x slower                                             |
| sqlglot_normalize       | 105 ms                                                                 | 110 ms: 1.05x slower                                              |
| logging_format          | 6.28 us                                                                | 6.59 us: 1.05x slower                                             |
| deepcopy_reduce         | 2.88 us                                                                | 3.02 us: 1.05x slower                                             |
| pickle_pure_python      | 281 us                                                                 | 295 us: 1.05x slower                                              |
| dask                    | 491 ms                                                                 | 516 ms: 1.05x slower                                              |
| scimark_monte_carlo     | 64.2 ms                                                                | 68.1 ms: 1.06x slower                                             |
| raytrace                | 282 ms                                                                 | 301 ms: 1.06x slower                                              |
| async_tree_memoization  | 622 ms                                                                 | 670 ms: 1.08x slower                                              |
| coroutines              | 24.7 ms                                                                | 26.8 ms: 1.09x slower                                             |
| sympy_integrate         | 20.2 ms                                                                | 22.1 ms: 1.09x slower                                             |
| gc_traversal            | 3.57 ms                                                                | 4.15 ms: 1.16x slower                                             |
| Geometric mean          | (ref)                                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (14): telco, pickle_list, thrift, mako, bench_mp_pool, regex_effbot, json, xml_etree_parse, nbody, async_tree_none, djangocms, coverage, scimark_sparse_mat_mult, mypy
