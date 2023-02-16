
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b8b1879
- commit date: 2023-02-05
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 60.2 ms: 1.08x faster                                               |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.9 ms: 1.05x faster                                               |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                                |
| nbody          | 90.0 ms                                                | 99.5 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                               |
| regex_effbot   | 3.46 ms                                                | 3.62 ms: 1.05x slower                                               |
| regex_dna      | 203 ms                                                 | 214 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                               |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.14x faster                                                |
| json_loads           | 26.1 us                                                | 23.5 us: 1.11x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.08x faster                                                |
| pickle_list          | 4.14 us                                                | 4.00 us: 1.04x faster                                               |
| pickle_dict          | 31.2 us                                                | 30.1 us: 1.03x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.84 us: 1.03x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pickle               | 9.90 us                                                | 9.98 us: 1.01x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 78.1 ms: 1.03x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.92 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.46 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.7 ms: 1.08x faster                                               |
| mako            | 9.83 ms                                                | 9.62 ms: 1.02x faster                                               |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                               |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 493 ms: 1.79x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.92 ms: 1.17x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.14x faster                                                |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                               |
| json_loads              | 26.1 us                                                | 23.5 us: 1.11x faster                                               |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                |
| richards                | 46.1 ms                                                | 42.4 ms: 1.09x faster                                               |
| nqueens                 | 83.8 ms                                                | 77.0 ms: 1.09x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| chaos                   | 68.7 ms                                                | 63.2 ms: 1.09x faster                                               |
| genshi_xml              | 51.4 ms                                                | 47.7 ms: 1.08x faster                                               |
| html5lib                | 64.8 ms                                                | 60.2 ms: 1.08x faster                                               |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.08x faster                                                |
| sympy_str               | 291 ms                                                 | 272 ms: 1.07x faster                                                |
| json                    | 4.87 ms                                                | 4.55 ms: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| logging_silent          | 98.0 ns                                                | 92.6 ns: 1.06x faster                                               |
| mdp                     | 2.63 sec                                               | 2.49 sec: 1.06x faster                                              |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                                |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                              |
| float                   | 76.8 ms                                                | 72.9 ms: 1.05x faster                                               |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                |
| coroutines              | 26.2 ms                                                | 24.9 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 999 us: 1.05x faster                                                |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                                |
| bench_thread_pool       | 817 us                                                 | 780 us: 1.05x faster                                                |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.05x faster                                               |
| logging_simple          | 6.02 us                                                | 5.76 us: 1.04x faster                                               |
| pyflate                 | 419 ms                                                 | 401 ms: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| pickle_list             | 4.14 us                                                | 4.00 us: 1.04x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                              |
| pickle_dict             | 31.2 us                                                | 30.1 us: 1.03x faster                                               |
| spectral_norm           | 98.1 ms                                                | 95.0 ms: 1.03x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.84 us: 1.03x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| unpack_sequence         | 44.5 ns                                                | 43.2 ns: 1.03x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                                |
| sqlglot_optimize        | 52.7 ms                                                | 51.3 ms: 1.03x faster                                               |
| dulwich_log             | 64.0 ms                                                | 62.4 ms: 1.03x faster                                               |
| thrift                  | 760 us                                                 | 741 us: 1.02x faster                                                |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                               |
| mako                    | 9.83 ms                                                | 9.62 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| async_generators        | 356 ms                                                 | 349 ms: 1.02x faster                                                |
| raytrace                | 291 ms                                                 | 287 ms: 1.02x faster                                                |
| gc_traversal            | 3.82 ms                                                | 3.76 ms: 1.02x faster                                               |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                               |
| deepcopy                | 341 us                                                 | 336 us: 1.02x faster                                                |
| logging_format          | 6.48 us                                                | 6.38 us: 1.02x faster                                               |
| crypto_pyaes            | 75.7 ms                                                | 75.2 ms: 1.01x faster                                               |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                               |
| pickle                  | 9.90 us                                                | 9.98 us: 1.01x slower                                               |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                               |
| scimark_lu              | 108 ms                                                 | 109 ms: 1.01x slower                                                |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.55 us: 1.03x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 78.1 ms: 1.03x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 762 ms: 1.04x slower                                                |
| python_startup          | 8.58 ms                                                | 8.92 ms: 1.04x slower                                               |
| generators              | 73.5 ms                                                | 76.8 ms: 1.04x slower                                               |
| regex_effbot            | 3.46 ms                                                | 3.62 ms: 1.05x slower                                               |
| regex_dna               | 203 ms                                                 | 214 ms: 1.05x slower                                                |
| async_tree_memoization  | 624 ms                                                 | 659 ms: 1.06x slower                                                |
| python_startup_no_site  | 6.04 ms                                                | 6.46 ms: 1.07x slower                                               |
| nbody                   | 90.0 ms                                                | 99.5 ms: 1.11x slower                                               |
| dask                    | 365 ms                                                 | 497 ms: 1.36x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (12): unpickle, chameleon, deepcopy_reduce, coverage, scimark_monte_carlo, telco, pathlib, bench_mp_pool, async_tree_none, xml_etree_process, meteor_contest, djangocms
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230205-3.12.0a4+-b8b1879/bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879.json: mypy
