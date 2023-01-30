
# Results vs. 3.10.4

- fork: mdboom
- ref: RegCPython
- machine: linux-x86_64
- commit hash: 53f2d50
- commit date: 2022-07-20
- overall geometric mean: 1.05x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 313 ms: 1.06x faster                                      |
| chameleon      | 8.86 ms                                                | 8.49 ms: 1.04x faster                                     |
| docutils       | 3.18 sec                                               | 3.10 sec: 1.03x faster                                    |
| html5lib       | 85.8 ms                                                | 76.8 ms: 1.12x faster                                     |
| tornado_http   | 128 ms                                                 | 123 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| nbody          | 136 ms                                                 | 101 ms: 1.35x faster                                      |
| float          | 108 ms                                                 | 94.9 ms: 1.14x faster                                     |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.16x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 157 ms: 1.11x faster                                      |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                      |
| regex_v8       | 25.0 ms                                                | 25.3 ms: 1.02x slower                                     |
| regex_effbot   | 3.21 ms                                                | 3.31 ms: 1.03x slower                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| xml_etree_generate   | 93.3 ms                                                | 86.2 ms: 1.08x faster                                     |
| xml_etree_process    | 74.5 ms                                                | 68.9 ms: 1.08x faster                                     |
| unpickle_pure_python | 297 us                                                 | 279 us: 1.06x faster                                      |
| pickle_pure_python   | 453 us                                                 | 432 us: 1.05x faster                                      |
| pickle_dict          | 28.3 us                                                | 27.2 us: 1.04x faster                                     |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                      |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.04x faster                                      |
| unpickle_list        | 4.99 us                                                | 4.86 us: 1.03x faster                                     |
| json_dumps           | 13.5 ms                                                | 13.4 ms: 1.01x faster                                     |
| json_loads           | 28.9 us                                                | 29.0 us: 1.01x slower                                     |
| pickle_list          | 4.50 us                                                | 4.65 us: 1.03x slower                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                              |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 5.76 ms                                                | 5.80 ms: 1.01x slower                                     |
| python_startup         | 13.9 ms                                                | 15.2 ms: 1.09x slower                                     |
| Geometric mean         | (ref)                                                  | 1.05x slower                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 14.3 ms                                                | 13.1 ms: 1.09x faster                                     |
| genshi_text     | 30.6 ms                                                | 29.0 ms: 1.06x faster                                     |
| genshi_xml      | 63.6 ms                                                | 60.6 ms: 1.05x faster                                     |
| django_template | 46.3 ms                                                | 48.4 ms: 1.05x slower                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| nbody                   | 136 ms                                                 | 101 ms: 1.35x faster                                      |
| generators              | 75.8 ms                                                | 56.3 ms: 1.35x faster                                     |
| fannkuch                | 477 ms                                                 | 369 ms: 1.29x faster                                      |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.29 ms: 1.28x faster                                     |
| scimark_fft             | 414 ms                                                 | 337 ms: 1.23x faster                                      |
| scimark_monte_carlo     | 105 ms                                                 | 85.8 ms: 1.22x faster                                     |
| spectral_norm           | 148 ms                                                 | 124 ms: 1.19x faster                                      |
| pyflate                 | 675 ms                                                 | 580 ms: 1.16x faster                                      |
| chaos                   | 104 ms                                                 | 91.1 ms: 1.14x faster                                     |
| float                   | 108 ms                                                 | 94.9 ms: 1.14x faster                                     |
| unpack_sequence         | 59.5 ns                                                | 52.8 ns: 1.13x faster                                     |
| nqueens                 | 99.3 ms                                                | 88.6 ms: 1.12x faster                                     |
| hexiom                  | 9.42 ms                                                | 8.43 ms: 1.12x faster                                     |
| go                      | 226 ms                                                 | 203 ms: 1.12x faster                                      |
| html5lib                | 85.8 ms                                                | 76.8 ms: 1.12x faster                                     |
| crypto_pyaes            | 118 ms                                                 | 106 ms: 1.11x faster                                      |
| deepcopy_memo           | 50.0 us                                                | 45.1 us: 1.11x faster                                     |
| regex_compile           | 174 ms                                                 | 157 ms: 1.11x faster                                      |
| coroutines              | 31.7 ms                                                | 28.6 ms: 1.11x faster                                     |
| pycparser               | 1.51 sec                                               | 1.37 sec: 1.11x faster                                    |
| async_tree_io           | 1.78 sec                                               | 1.61 sec: 1.10x faster                                    |
| scimark_sor             | 193 ms                                                 | 176 ms: 1.09x faster                                      |
| mako                    | 14.3 ms                                                | 13.1 ms: 1.09x faster                                     |
| xml_etree_generate      | 93.3 ms                                                | 86.2 ms: 1.08x faster                                     |
| xml_etree_process       | 74.5 ms                                                | 68.9 ms: 1.08x faster                                     |
| gunicorn                | 1.43 ms                                                | 1.33 ms: 1.08x faster                                     |
| aiohttp                 | 1.34 ms                                                | 1.25 ms: 1.07x faster                                     |
| telco                   | 6.68 ms                                                | 6.27 ms: 1.07x faster                                     |
| deepcopy                | 429 us                                                 | 404 us: 1.06x faster                                      |
| unpickle_pure_python    | 297 us                                                 | 279 us: 1.06x faster                                      |
| 2to3                    | 332 ms                                                 | 313 ms: 1.06x faster                                      |
| dulwich_log             | 75.5 ms                                                | 71.2 ms: 1.06x faster                                     |
| logging_format          | 8.92 us                                                | 8.42 us: 1.06x faster                                     |
| sqlalchemy_imperative   | 21.0 ms                                                | 19.9 ms: 1.06x faster                                     |
| deepcopy_reduce         | 3.75 us                                                | 3.55 us: 1.06x faster                                     |
| genshi_text             | 30.6 ms                                                | 29.0 ms: 1.06x faster                                     |
| richards                | 71.4 ms                                                | 67.6 ms: 1.06x faster                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.93 ms: 1.06x faster                                     |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.05x faster                                      |
| pickle_pure_python      | 453 us                                                 | 432 us: 1.05x faster                                      |
| genshi_xml              | 63.6 ms                                                | 60.6 ms: 1.05x faster                                     |
| pprint_pformat          | 1.97 sec                                               | 1.88 sec: 1.05x faster                                    |
| sqlglot_transpile       | 2.42 ms                                                | 2.31 ms: 1.05x faster                                     |
| raytrace                | 461 ms                                                 | 440 ms: 1.05x faster                                      |
| tornado_http            | 128 ms                                                 | 123 ms: 1.04x faster                                      |
| chameleon               | 8.86 ms                                                | 8.49 ms: 1.04x faster                                     |
| sympy_integrate         | 23.9 ms                                                | 22.9 ms: 1.04x faster                                     |
| pickle_dict             | 28.3 us                                                | 27.2 us: 1.04x faster                                     |
| flaskblogging           | 8.38 ms                                                | 8.07 ms: 1.04x faster                                     |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                      |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.04x faster                                      |
| scimark_lu              | 158 ms                                                 | 153 ms: 1.03x faster                                      |
| pprint_safe_repr        | 943 ms                                                 | 914 ms: 1.03x faster                                      |
| mdp                     | 2.82 sec                                               | 2.74 sec: 1.03x faster                                    |
| unpickle_list           | 4.99 us                                                | 4.86 us: 1.03x faster                                     |
| docutils                | 3.18 sec                                               | 3.10 sec: 1.03x faster                                    |
| sympy_str               | 324 ms                                                 | 316 ms: 1.03x faster                                      |
| deltablue               | 7.39 ms                                                | 7.24 ms: 1.02x faster                                     |
| logging_simple          | 8.06 us                                                | 7.90 us: 1.02x faster                                     |
| async_tree_memoization  | 854 ms                                                 | 839 ms: 1.02x faster                                      |
| pylint                  | 519 ms                                                 | 512 ms: 1.01x faster                                      |
| sympy_sum               | 183 ms                                                 | 181 ms: 1.01x faster                                      |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 164 ms: 1.01x faster                                      |
| json_dumps              | 13.5 ms                                                | 13.4 ms: 1.01x faster                                     |
| sympy_expand            | 537 ms                                                 | 533 ms: 1.01x faster                                      |
| bench_thread_pool       | 943 us                                                 | 947 us: 1.00x slower                                      |
| json_loads              | 28.9 us                                                | 29.0 us: 1.01x slower                                     |
| python_startup_no_site  | 5.76 ms                                                | 5.80 ms: 1.01x slower                                     |
| sqlite_synth            | 2.90 us                                                | 2.93 us: 1.01x slower                                     |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                      |
| regex_v8                | 25.0 ms                                                | 25.3 ms: 1.02x slower                                     |
| sqlglot_optimize        | 65.3 ms                                                | 66.5 ms: 1.02x slower                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 970 ms: 1.02x slower                                      |
| pickle_list             | 4.50 us                                                | 4.65 us: 1.03x slower                                     |
| sqlglot_normalize       | 135 ms                                                 | 139 ms: 1.03x slower                                      |
| regex_effbot            | 3.21 ms                                                | 3.31 ms: 1.03x slower                                     |
| django_template         | 46.3 ms                                                | 48.4 ms: 1.05x slower                                     |
| python_startup          | 13.9 ms                                                | 15.2 ms: 1.09x slower                                     |
| logging_silent          | 173 ns                                                 | 194 ns: 1.12x slower                                      |
| async_generators        | 428 ms                                                 | 495 ms: 1.16x slower                                      |
| Geometric mean          | (ref)                                                  | 1.05x faster                                              |

Benchmark hidden because not significant (8): mypy, pickle, thrift, bench_mp_pool, unpickle, json, pathlib, async_tree_none
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220720-3.10.1-53f2d50/bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal
