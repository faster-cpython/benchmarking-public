
# Results vs. base

- fork: iritkatriel
- ref: const_regs2
- machine: linux-x86_64
- commit hash: 1c97383
- commit date: 2023-01-17
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 259 ms: 1.02x slower                                               |
| chameleon      | 6.31 ms                                                                | 6.47 ms: 1.03x slower                                              |
| docutils       | 2.50 sec                                                               | 2.61 sec: 1.05x slower                                             |
| html5lib       | 59.5 ms                                                                | 60.7 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 95.0 ms                                                                | 96.2 ms: 1.01x slower                                              |
| pidigits       | 192 ms                                                                 | 198 ms: 1.03x slower                                               |
| float          | 72.1 ms                                                                | 74.9 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.60 ms                                                                | 3.47 ms: 1.04x faster                                              |
| regex_dna      | 211 ms                                                                 | 210 ms: 1.00x faster                                               |
| regex_v8       | 22.0 ms                                                                | 22.6 ms: 1.03x slower                                              |
| regex_compile  | 129 ms                                                                 | 134 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse  | 109 ms                                                                 | 103 ms: 1.05x faster                                               |
| unpickle_list        | 4.98 us                                                                | 4.88 us: 1.02x faster                                              |
| pickle_dict          | 30.4 us                                                                | 30.7 us: 1.01x slower                                              |
| json_loads           | 23.8 us                                                                | 24.2 us: 1.01x slower                                              |
| json_dumps           | 9.37 ms                                                                | 9.51 ms: 1.02x slower                                              |
| xml_etree_process    | 53.8 ms                                                                | 54.9 ms: 1.02x slower                                              |
| pickle_list          | 4.07 us                                                                | 4.17 us: 1.02x slower                                              |
| unpickle_pure_python | 200 us                                                                 | 205 us: 1.03x slower                                               |
| xml_etree_generate   | 76.8 ms                                                                | 78.8 ms: 1.03x slower                                              |
| unpickle             | 12.9 us                                                                | 13.5 us: 1.05x slower                                              |
| pickle_pure_python   | 281 us                                                                 | 299 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (2): pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.06 ms                                                                | 6.13 ms: 1.01x slower                                              |
| python_startup         | 8.50 ms                                                                | 8.60 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.78 ms                                                                | 9.85 ms: 1.01x slower                                              |
| genshi_xml      | 46.5 ms                                                                | 47.8 ms: 1.03x slower                                              |
| genshi_text     | 20.2 ms                                                                | 20.8 ms: 1.03x slower                                              |
| django_template | 32.3 ms                                                                | 34.5 ms: 1.07x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse     | 109 ms                                                                 | 103 ms: 1.05x faster                                               |
| unpack_sequence         | 43.8 ns                                                                | 41.7 ns: 1.05x faster                                              |
| regex_effbot            | 3.60 ms                                                                | 3.47 ms: 1.04x faster                                              |
| unpickle_list           | 4.98 us                                                                | 4.88 us: 1.02x faster                                              |
| nqueens                 | 79.6 ms                                                                | 78.9 ms: 1.01x faster                                              |
| regex_dna               | 211 ms                                                                 | 210 ms: 1.00x faster                                               |
| asyncio_tcp             | 503 ms                                                                 | 505 ms: 1.00x slower                                               |
| sqlite_synth            | 2.57 us                                                                | 2.59 us: 1.01x slower                                              |
| generators              | 79.3 ms                                                                | 79.9 ms: 1.01x slower                                              |
| mako                    | 9.78 ms                                                                | 9.85 ms: 1.01x slower                                              |
| scimark_fft             | 312 ms                                                                 | 315 ms: 1.01x slower                                               |
| pickle_dict             | 30.4 us                                                                | 30.7 us: 1.01x slower                                              |
| create_gc_cycles        | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                              |
| crypto_pyaes            | 75.1 ms                                                                | 75.9 ms: 1.01x slower                                              |
| python_startup_no_site  | 6.06 ms                                                                | 6.13 ms: 1.01x slower                                              |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 4.07 ms: 1.01x slower                                              |
| python_startup          | 8.50 ms                                                                | 8.60 ms: 1.01x slower                                              |
| nbody                   | 95.0 ms                                                                | 96.2 ms: 1.01x slower                                              |
| json_loads              | 23.8 us                                                                | 24.2 us: 1.01x slower                                              |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                             |
| json_dumps              | 9.37 ms                                                                | 9.51 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed | 753 ms                                                                 | 765 ms: 1.02x slower                                               |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.02x slower                                             |
| json                    | 4.66 ms                                                                | 4.74 ms: 1.02x slower                                              |
| async_tree_none         | 525 ms                                                                 | 534 ms: 1.02x slower                                               |
| xml_etree_process       | 53.8 ms                                                                | 54.9 ms: 1.02x slower                                              |
| html5lib                | 59.5 ms                                                                | 60.7 ms: 1.02x slower                                              |
| 2to3                    | 253 ms                                                                 | 259 ms: 1.02x slower                                               |
| bench_thread_pool       | 782 us                                                                 | 801 us: 1.02x slower                                               |
| pickle_list             | 4.07 us                                                                | 4.17 us: 1.02x slower                                              |
| pathlib                 | 17.8 ms                                                                | 18.3 ms: 1.03x slower                                              |
| chameleon               | 6.31 ms                                                                | 6.47 ms: 1.03x slower                                              |
| pidigits                | 192 ms                                                                 | 198 ms: 1.03x slower                                               |
| unpickle_pure_python    | 200 us                                                                 | 205 us: 1.03x slower                                               |
| xml_etree_generate      | 76.8 ms                                                                | 78.8 ms: 1.03x slower                                              |
| scimark_lu              | 107 ms                                                                 | 110 ms: 1.03x slower                                               |
| coverage                | 98.4 ms                                                                | 101 ms: 1.03x slower                                               |
| genshi_xml              | 46.5 ms                                                                | 47.8 ms: 1.03x slower                                              |
| genshi_text             | 20.2 ms                                                                | 20.8 ms: 1.03x slower                                              |
| scimark_monte_carlo     | 64.2 ms                                                                | 66.1 ms: 1.03x slower                                              |
| regex_v8                | 22.0 ms                                                                | 22.6 ms: 1.03x slower                                              |
| sympy_sum               | 162 ms                                                                 | 168 ms: 1.03x slower                                               |
| chaos                   | 66.7 ms                                                                | 69.0 ms: 1.03x slower                                              |
| pprint_pformat          | 1.38 sec                                                               | 1.43 sec: 1.04x slower                                             |
| regex_compile           | 129 ms                                                                 | 134 ms: 1.04x slower                                               |
| dulwich_log             | 62.0 ms                                                                | 64.3 ms: 1.04x slower                                              |
| sympy_expand            | 453 ms                                                                 | 470 ms: 1.04x slower                                               |
| sympy_str               | 280 ms                                                                 | 291 ms: 1.04x slower                                               |
| sqlglot_normalize       | 105 ms                                                                 | 109 ms: 1.04x slower                                               |
| sqlglot_optimize        | 51.0 ms                                                                | 53.0 ms: 1.04x slower                                              |
| float                   | 72.1 ms                                                                | 74.9 ms: 1.04x slower                                              |
| hexiom                  | 6.07 ms                                                                | 6.31 ms: 1.04x slower                                              |
| pyflate                 | 393 ms                                                                 | 409 ms: 1.04x slower                                               |
| spectral_norm           | 96.4 ms                                                                | 100 ms: 1.04x slower                                               |
| go                      | 136 ms                                                                 | 141 ms: 1.04x slower                                               |
| scimark_sor             | 106 ms                                                                 | 111 ms: 1.04x slower                                               |
| mdp                     | 2.44 sec                                                               | 2.55 sec: 1.04x slower                                             |
| sqlglot_transpile       | 1.71 ms                                                                | 1.78 ms: 1.04x slower                                              |
| sqlglot_parse           | 1.41 ms                                                                | 1.48 ms: 1.04x slower                                              |
| logging_format          | 6.28 us                                                                | 6.57 us: 1.05x slower                                              |
| docutils                | 2.50 sec                                                               | 2.61 sec: 1.05x slower                                             |
| pprint_safe_repr        | 666 ms                                                                 | 697 ms: 1.05x slower                                               |
| logging_simple          | 5.75 us                                                                | 6.01 us: 1.05x slower                                              |
| unpickle                | 12.9 us                                                                | 13.5 us: 1.05x slower                                              |
| logging_silent          | 93.9 ns                                                                | 98.6 ns: 1.05x slower                                              |
| coroutines              | 24.7 ms                                                                | 26.0 ms: 1.05x slower                                              |
| deltablue               | 3.24 ms                                                                | 3.42 ms: 1.05x slower                                              |
| deepcopy_memo           | 34.0 us                                                                | 35.8 us: 1.05x slower                                              |
| dask                    | 491 ms                                                                 | 519 ms: 1.06x slower                                               |
| deepcopy                | 331 us                                                                 | 350 us: 1.06x slower                                               |
| richards                | 41.9 ms                                                                | 44.4 ms: 1.06x slower                                              |
| pickle_pure_python      | 281 us                                                                 | 299 us: 1.06x slower                                               |
| raytrace                | 282 ms                                                                 | 301 ms: 1.06x slower                                               |
| django_template         | 32.3 ms                                                                | 34.5 ms: 1.07x slower                                              |
| async_tree_memoization  | 622 ms                                                                 | 667 ms: 1.07x slower                                               |
| deepcopy_reduce         | 2.88 us                                                                | 3.12 us: 1.08x slower                                              |
| sympy_integrate         | 20.2 ms                                                                | 22.1 ms: 1.10x slower                                              |
| gc_traversal            | 3.57 ms                                                                | 4.29 ms: 1.20x slower                                              |
| Geometric mean          | (ref)                                                                  | 1.03x slower                                                       |

Benchmark hidden because not significant (10): djangocms, async_generators, pickle, bench_mp_pool, fannkuch, thrift, meteor_contest, telco, xml_etree_parse, mypy
