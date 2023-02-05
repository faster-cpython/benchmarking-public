
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
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.34 ms: 1.01x faster                                               |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 63.2 ms                                                | 60.2 ms: 1.05x faster                                               |
| tornado_http   | 96.6 ms                                                | 94.3 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                                |
| float          | 76.3 ms                                                | 72.9 ms: 1.05x faster                                               |
| nbody          | 95.0 ms                                                | 99.5 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.01x slower                                               |
| regex_dna      | 203 ms                                                 | 214 ms: 1.05x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.62 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.51 ms: 1.33x faster                                               |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                |
| json_loads           | 26.2 us                                                | 23.5 us: 1.12x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                                |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                |
| pickle_list          | 4.17 us                                                | 4.00 us: 1.04x faster                                               |
| pickle_dict          | 31.4 us                                                | 30.1 us: 1.04x faster                                               |
| unpickle_list        | 4.95 us                                                | 4.84 us: 1.02x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| pickle               | 9.79 us                                                | 9.98 us: 1.02x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 78.1 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.92 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.46 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 47.7 ms: 1.09x faster                                               |
| genshi_text    | 22.1 ms                                                | 21.2 ms: 1.04x faster                                               |
| mako           | 9.85 ms                                                | 9.62 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.51 ms: 1.33x faster                                               |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.14x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.92 ms: 1.12x faster                                               |
| json_loads              | 26.2 us                                                | 23.5 us: 1.12x faster                                               |
| nqueens                 | 85.0 ms                                                | 77.0 ms: 1.10x faster                                               |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                |
| genshi_xml              | 52.1 ms                                                | 47.7 ms: 1.09x faster                                               |
| richards                | 46.2 ms                                                | 42.4 ms: 1.09x faster                                               |
| json                    | 4.95 ms                                                | 4.55 ms: 1.09x faster                                               |
| chaos                   | 68.6 ms                                                | 63.2 ms: 1.09x faster                                               |
| go                      | 143 ms                                                 | 133 ms: 1.07x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                                |
| scimark_fft             | 329 ms                                                 | 309 ms: 1.07x faster                                                |
| logging_silent          | 98.5 ns                                                | 92.6 ns: 1.06x faster                                               |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                |
| hexiom                  | 6.35 ms                                                | 5.98 ms: 1.06x faster                                               |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                                |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| sympy_str               | 287 ms                                                 | 272 ms: 1.06x faster                                                |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                              |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                               |
| logging_simple          | 6.06 us                                                | 5.76 us: 1.05x faster                                               |
| spectral_norm           | 99.9 ms                                                | 95.0 ms: 1.05x faster                                               |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                               |
| html5lib                | 63.2 ms                                                | 60.2 ms: 1.05x faster                                               |
| coroutines              | 26.1 ms                                                | 24.9 ms: 1.05x faster                                               |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                | 999 us: 1.05x faster                                                |
| float                   | 76.3 ms                                                | 72.9 ms: 1.05x faster                                               |
| pickle_list             | 4.17 us                                                | 4.00 us: 1.04x faster                                               |
| genshi_text             | 22.1 ms                                                | 21.2 ms: 1.04x faster                                               |
| pickle_dict             | 31.4 us                                                | 30.1 us: 1.04x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| pycparser               | 1.17 sec                                               | 1.13 sec: 1.04x faster                                              |
| pyflate                 | 417 ms                                                 | 401 ms: 1.04x faster                                                |
| bench_thread_pool       | 810 us                                                 | 780 us: 1.04x faster                                                |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| logging_format          | 6.62 us                                                | 6.38 us: 1.04x faster                                               |
| sqlglot_optimize        | 53.0 ms                                                | 51.3 ms: 1.03x faster                                               |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                |
| telco                   | 6.62 ms                                                | 6.42 ms: 1.03x faster                                               |
| async_generators        | 359 ms                                                 | 349 ms: 1.03x faster                                                |
| pprint_pformat          | 1.44 sec                                               | 1.41 sec: 1.03x faster                                              |
| tornado_http            | 96.6 ms                                                | 94.3 ms: 1.03x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.4 ms: 1.02x faster                                               |
| unpickle_list           | 4.95 us                                                | 4.84 us: 1.02x faster                                               |
| mako                    | 9.85 ms                                                | 9.62 ms: 1.02x faster                                               |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| deepcopy                | 344 us                                                 | 336 us: 1.02x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| coverage                | 101 ms                                                 | 98.9 ms: 1.02x faster                                               |
| thrift                  | 752 us                                                 | 741 us: 1.01x faster                                                |
| raytrace                | 290 ms                                                 | 287 ms: 1.01x faster                                                |
| chameleon               | 6.41 ms                                                | 6.34 ms: 1.01x faster                                               |
| scimark_monte_carlo     | 68.3 ms                                                | 67.7 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| pprint_safe_repr        | 691 ms                                                 | 686 ms: 1.01x faster                                                |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                               |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.01x slower                                               |
| deepcopy_reduce         | 2.97 us                                                | 3.01 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed | 752 ms                                                 | 762 ms: 1.01x slower                                                |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                              |
| crypto_pyaes            | 73.9 ms                                                | 75.2 ms: 1.02x slower                                               |
| scimark_lu              | 107 ms                                                 | 109 ms: 1.02x slower                                                |
| pickle                  | 9.79 us                                                | 9.98 us: 1.02x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.55 us: 1.02x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 78.1 ms: 1.02x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                               |
| nbody                   | 95.0 ms                                                | 99.5 ms: 1.05x slower                                               |
| regex_dna               | 203 ms                                                 | 214 ms: 1.05x slower                                                |
| async_tree_memoization  | 625 ms                                                 | 659 ms: 1.05x slower                                                |
| generators              | 72.2 ms                                                | 76.8 ms: 1.06x slower                                               |
| python_startup          | 8.36 ms                                                | 8.92 ms: 1.07x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.62 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.46 ms: 1.08x slower                                               |
| mypy                    | 669 ms                                                 | 805 ms: 1.20x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (7): unpickle, unpack_sequence, async_tree_none, bench_mp_pool, meteor_contest, xml_etree_process, django_template
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230205-3.12.0a4+-b8b1879/bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
