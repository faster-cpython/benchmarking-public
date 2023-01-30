
# Results vs. 3.11.0

- fork: mdboom
- ref: RegCPython
- machine: linux-x86_64
- commit hash: 53f2d50
- commit date: 2022-07-20
- overall geometric mean: 1.20x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 313 ms: 1.22x slower                                      |
| chameleon      | 6.41 ms                                                | 8.49 ms: 1.32x slower                                     |
| docutils       | 2.60 sec                                               | 3.10 sec: 1.19x slower                                    |
| html5lib       | 63.2 ms                                                | 76.8 ms: 1.22x slower                                     |
| tornado_http   | 96.6 ms                                                | 123 ms: 1.27x slower                                      |
| Geometric mean | (ref)                                                  | 1.24x slower                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 188 ms: 1.06x faster                                      |
| nbody          | 95.0 ms                                                | 101 ms: 1.06x slower                                      |
| float          | 76.3 ms                                                | 94.9 ms: 1.24x slower                                     |
| Geometric mean | (ref)                                                  | 1.08x slower                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 3.36 ms                                                | 3.31 ms: 1.01x faster                                     |
| regex_dna      | 203 ms                                                 | 216 ms: 1.06x slower                                      |
| regex_v8       | 22.3 ms                                                | 25.3 ms: 1.14x slower                                     |
| regex_compile  | 136 ms                                                 | 157 ms: 1.15x slower                                      |
| Geometric mean | (ref)                                                  | 1.08x slower                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pickle_dict          | 31.4 us                                                | 27.2 us: 1.15x faster                                     |
| unpickle_list        | 4.95 us                                                | 4.86 us: 1.02x faster                                     |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                     |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.04x slower                                      |
| json_dumps           | 12.7 ms                                                | 13.4 ms: 1.05x slower                                     |
| unpickle             | 13.3 us                                                | 14.3 us: 1.08x slower                                     |
| json_loads           | 26.2 us                                                | 29.0 us: 1.11x slower                                     |
| pickle_list          | 4.17 us                                                | 4.65 us: 1.11x slower                                     |
| xml_etree_generate   | 76.2 ms                                                | 86.2 ms: 1.13x slower                                     |
| unpickle_pure_python | 225 us                                                 | 279 us: 1.24x slower                                      |
| xml_etree_process    | 53.8 ms                                                | 68.9 ms: 1.28x slower                                     |
| pickle_pure_python   | 304 us                                                 | 432 us: 1.42x slower                                      |
| Geometric mean       | (ref)                                                  | 1.09x slower                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 5.80 ms: 1.03x faster                                     |
| python_startup         | 8.36 ms                                                | 15.2 ms: 1.82x slower                                     |
| Geometric mean         | (ref)                                                  | 1.33x slower                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 60.6 ms: 1.16x slower                                     |
| genshi_text     | 22.1 ms                                                | 29.0 ms: 1.31x slower                                     |
| mako            | 9.85 ms                                                | 13.1 ms: 1.33x slower                                     |
| django_template | 32.5 ms                                                | 48.4 ms: 1.49x slower                                     |
| Geometric mean  | (ref)                                                  | 1.32x slower                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| generators              | 72.2 ms                                                | 56.3 ms: 1.28x faster                                     |
| pickle_dict             | 31.4 us                                                | 27.2 us: 1.15x faster                                     |
| pidigits                | 199 ms                                                 | 188 ms: 1.06x faster                                      |
| telco                   | 6.62 ms                                                | 6.27 ms: 1.06x faster                                     |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                      |
| python_startup_no_site  | 5.96 ms                                                | 5.80 ms: 1.03x faster                                     |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.29 ms: 1.03x faster                                     |
| unpickle_list           | 4.95 us                                                | 4.86 us: 1.02x faster                                     |
| regex_effbot            | 3.36 ms                                                | 3.31 ms: 1.01x faster                                     |
| scimark_fft             | 329 ms                                                 | 337 ms: 1.02x slower                                      |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                     |
| meteor_contest          | 105 ms                                                 | 108 ms: 1.03x slower                                      |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.04x slower                                      |
| nqueens                 | 85.0 ms                                                | 88.6 ms: 1.04x slower                                     |
| mdp                     | 2.62 sec                                               | 2.74 sec: 1.04x slower                                    |
| json_dumps              | 12.7 ms                                                | 13.4 ms: 1.05x slower                                     |
| regex_dna               | 203 ms                                                 | 216 ms: 1.06x slower                                      |
| nbody                   | 95.0 ms                                                | 101 ms: 1.06x slower                                      |
| unpickle                | 13.3 us                                                | 14.3 us: 1.08x slower                                     |
| json                    | 4.95 ms                                                | 5.37 ms: 1.08x slower                                     |
| sympy_sum               | 166 ms                                                 | 181 ms: 1.09x slower                                      |
| coroutines              | 26.1 ms                                                | 28.6 ms: 1.10x slower                                     |
| sympy_str               | 287 ms                                                 | 316 ms: 1.10x slower                                      |
| sympy_integrate         | 20.9 ms                                                | 22.9 ms: 1.10x slower                                     |
| sqlalchemy_imperative   | 18.0 ms                                                | 19.9 ms: 1.10x slower                                     |
| pylint                  | 463 ms                                                 | 512 ms: 1.11x slower                                      |
| pathlib                 | 18.2 ms                                                | 20.1 ms: 1.11x slower                                     |
| json_loads              | 26.2 us                                                | 29.0 us: 1.11x slower                                     |
| pickle_list             | 4.17 us                                                | 4.65 us: 1.11x slower                                     |
| dulwich_log             | 63.9 ms                                                | 71.2 ms: 1.11x slower                                     |
| sympy_expand            | 472 ms                                                 | 533 ms: 1.13x slower                                      |
| xml_etree_generate      | 76.2 ms                                                | 86.2 ms: 1.13x slower                                     |
| regex_v8                | 22.3 ms                                                | 25.3 ms: 1.14x slower                                     |
| flaskblogging           | 7.08 ms                                                | 8.07 ms: 1.14x slower                                     |
| regex_compile           | 136 ms                                                 | 157 ms: 1.15x slower                                      |
| genshi_xml              | 52.1 ms                                                | 60.6 ms: 1.16x slower                                     |
| pycparser               | 1.17 sec                                               | 1.37 sec: 1.17x slower                                    |
| bench_thread_pool       | 810 us                                                 | 947 us: 1.17x slower                                      |
| sqlite_synth            | 2.49 us                                                | 2.93 us: 1.17x slower                                     |
| deepcopy                | 344 us                                                 | 404 us: 1.17x slower                                      |
| sqlalchemy_declarative  | 139 ms                                                 | 164 ms: 1.18x slower                                      |
| gunicorn                | 1.12 ms                                                | 1.33 ms: 1.18x slower                                     |
| docutils                | 2.60 sec                                               | 3.10 sec: 1.19x slower                                    |
| aiohttp                 | 1.05 ms                                                | 1.25 ms: 1.19x slower                                     |
| deepcopy_reduce         | 2.97 us                                                | 3.55 us: 1.20x slower                                     |
| html5lib                | 63.2 ms                                                | 76.8 ms: 1.22x slower                                     |
| unpack_sequence         | 43.4 ns                                                | 52.8 ns: 1.22x slower                                     |
| 2to3                    | 257 ms                                                 | 313 ms: 1.22x slower                                      |
| async_tree_io           | 1.31 sec                                               | 1.61 sec: 1.23x slower                                    |
| deepcopy_memo           | 36.4 us                                                | 45.1 us: 1.24x slower                                     |
| unpickle_pure_python    | 225 us                                                 | 279 us: 1.24x slower                                      |
| spectral_norm           | 99.9 ms                                                | 124 ms: 1.24x slower                                      |
| float                   | 76.3 ms                                                | 94.9 ms: 1.24x slower                                     |
| sqlglot_optimize        | 53.0 ms                                                | 66.5 ms: 1.26x slower                                     |
| scimark_monte_carlo     | 68.3 ms                                                | 85.8 ms: 1.26x slower                                     |
| tornado_http            | 96.6 ms                                                | 123 ms: 1.27x slower                                      |
| logging_format          | 6.62 us                                                | 8.42 us: 1.27x slower                                     |
| xml_etree_process       | 53.8 ms                                                | 68.9 ms: 1.28x slower                                     |
| async_tree_cpu_io_mixed | 752 ms                                                 | 970 ms: 1.29x slower                                      |
| sqlglot_normalize       | 108 ms                                                 | 139 ms: 1.29x slower                                      |
| logging_simple          | 6.06 us                                                | 7.90 us: 1.30x slower                                     |
| pprint_pformat          | 1.44 sec                                               | 1.88 sec: 1.30x slower                                    |
| genshi_text             | 22.1 ms                                                | 29.0 ms: 1.31x slower                                     |
| pprint_safe_repr        | 691 ms                                                 | 914 ms: 1.32x slower                                      |
| chameleon               | 6.41 ms                                                | 8.49 ms: 1.32x slower                                     |
| hexiom                  | 6.35 ms                                                | 8.43 ms: 1.33x slower                                     |
| chaos                   | 68.6 ms                                                | 91.1 ms: 1.33x slower                                     |
| mako                    | 9.85 ms                                                | 13.1 ms: 1.33x slower                                     |
| async_tree_memoization  | 625 ms                                                 | 839 ms: 1.34x slower                                      |
| async_tree_none         | 529 ms                                                 | 724 ms: 1.37x slower                                      |
| thrift                  | 752 us                                                 | 1.03 ms: 1.37x slower                                     |
| async_generators        | 359 ms                                                 | 495 ms: 1.38x slower                                      |
| sqlglot_transpile       | 1.66 ms                                                | 2.31 ms: 1.39x slower                                     |
| pyflate                 | 417 ms                                                 | 580 ms: 1.39x slower                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.93 ms: 1.41x slower                                     |
| go                      | 143 ms                                                 | 203 ms: 1.41x slower                                      |
| pickle_pure_python      | 304 us                                                 | 432 us: 1.42x slower                                      |
| scimark_lu              | 107 ms                                                 | 153 ms: 1.42x slower                                      |
| crypto_pyaes            | 73.9 ms                                                | 106 ms: 1.43x slower                                      |
| richards                | 46.2 ms                                                | 67.6 ms: 1.46x slower                                     |
| mypy                    | 669 ms                                                 | 983 ms: 1.47x slower                                      |
| django_template         | 32.5 ms                                                | 48.4 ms: 1.49x slower                                     |
| raytrace                | 290 ms                                                 | 440 ms: 1.52x slower                                      |
| scimark_sor             | 115 ms                                                 | 176 ms: 1.53x slower                                      |
| python_startup          | 8.36 ms                                                | 15.2 ms: 1.82x slower                                     |
| logging_silent          | 98.5 ns                                                | 194 ns: 1.97x slower                                      |
| deltablue               | 3.64 ms                                                | 7.24 ms: 1.99x slower                                     |
| Geometric mean          | (ref)                                                  | 1.20x slower                                              |

Benchmark hidden because not significant (2): xml_etree_parse, bench_mp_pool
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: coverage
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220720-3.10.1-53f2d50/bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal
