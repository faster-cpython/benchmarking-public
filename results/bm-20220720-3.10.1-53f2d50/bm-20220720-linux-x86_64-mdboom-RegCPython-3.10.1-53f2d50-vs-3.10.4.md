
# Results vs. 3.10.4

- fork: mdboom
- ref: RegCPython
- machine: linux-x86_64
- commit hash: 53f2d50
- commit date: 2022-07-20
- overall geometric mean: 1.06x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 313 ms: 1.07x faster                                      |
| chameleon      | 9.17 ms                                                | 8.49 ms: 1.08x faster                                     |
| docutils       | 3.18 sec                                               | 3.10 sec: 1.03x faster                                    |
| html5lib       | 85.9 ms                                                | 76.8 ms: 1.12x faster                                     |
| tornado_http   | 128 ms                                                 | 123 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| nbody          | 144 ms                                                 | 101 ms: 1.42x faster                                      |
| float          | 109 ms                                                 | 94.9 ms: 1.15x faster                                     |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 157 ms: 1.13x faster                                      |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                      |
| regex_v8       | 25.0 ms                                                | 25.3 ms: 1.01x slower                                     |
| regex_effbot   | 3.19 ms                                                | 3.31 ms: 1.04x slower                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| xml_etree_generate   | 93.8 ms                                                | 86.2 ms: 1.09x faster                                     |
| xml_etree_process    | 74.5 ms                                                | 68.9 ms: 1.08x faster                                     |
| unpickle_pure_python | 302 us                                                 | 279 us: 1.08x faster                                      |
| pickle_pure_python   | 452 us                                                 | 432 us: 1.05x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.04x faster                                      |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                      |
| pickle_list          | 4.72 us                                                | 4.65 us: 1.02x faster                                     |
| pickle_dict          | 27.6 us                                                | 27.2 us: 1.01x faster                                     |
| unpickle_list        | 4.92 us                                                | 4.86 us: 1.01x faster                                     |
| json_dumps           | 13.4 ms                                                | 13.4 ms: 1.01x faster                                     |
| json_loads           | 28.7 us                                                | 29.0 us: 1.01x slower                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                              |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 5.78 ms                                                | 5.80 ms: 1.00x slower                                     |
| python_startup         | 14.1 ms                                                | 15.2 ms: 1.08x slower                                     |
| Geometric mean         | (ref)                                                  | 1.04x slower                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 14.7 ms                                                | 13.1 ms: 1.12x faster                                     |
| genshi_text     | 30.6 ms                                                | 29.0 ms: 1.06x faster                                     |
| genshi_xml      | 63.7 ms                                                | 60.6 ms: 1.05x faster                                     |
| django_template | 46.3 ms                                                | 48.4 ms: 1.04x slower                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| nbody                   | 144 ms                                                 | 101 ms: 1.42x faster                                      |
| generators              | 76.4 ms                                                | 56.3 ms: 1.36x faster                                     |
| fannkuch                | 488 ms                                                 | 369 ms: 1.32x faster                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.29 ms: 1.27x faster                                     |
| scimark_monte_carlo     | 109 ms                                                 | 85.8 ms: 1.27x faster                                     |
| scimark_fft             | 421 ms                                                 | 337 ms: 1.25x faster                                      |
| spectral_norm           | 150 ms                                                 | 124 ms: 1.21x faster                                      |
| pyflate                 | 676 ms                                                 | 580 ms: 1.17x faster                                      |
| chaos                   | 106 ms                                                 | 91.1 ms: 1.16x faster                                     |
| float                   | 109 ms                                                 | 94.9 ms: 1.15x faster                                     |
| deepcopy_memo           | 51.7 us                                                | 45.1 us: 1.15x faster                                     |
| regex_compile           | 177 ms                                                 | 157 ms: 1.13x faster                                      |
| nqueens                 | 100 ms                                                 | 88.6 ms: 1.13x faster                                     |
| unpack_sequence         | 59.4 ns                                                | 52.8 ns: 1.12x faster                                     |
| pycparser               | 1.53 sec                                               | 1.37 sec: 1.12x faster                                    |
| hexiom                  | 9.43 ms                                                | 8.43 ms: 1.12x faster                                     |
| mako                    | 14.7 ms                                                | 13.1 ms: 1.12x faster                                     |
| html5lib                | 85.9 ms                                                | 76.8 ms: 1.12x faster                                     |
| scimark_sor             | 197 ms                                                 | 176 ms: 1.12x faster                                      |
| richards                | 75.2 ms                                                | 67.6 ms: 1.11x faster                                     |
| go                      | 226 ms                                                 | 203 ms: 1.11x faster                                      |
| async_tree_io           | 1.78 sec                                               | 1.61 sec: 1.11x faster                                    |
| coroutines              | 31.6 ms                                                | 28.6 ms: 1.11x faster                                     |
| crypto_pyaes            | 117 ms                                                 | 106 ms: 1.10x faster                                      |
| xml_etree_generate      | 93.8 ms                                                | 86.2 ms: 1.09x faster                                     |
| deepcopy                | 438 us                                                 | 404 us: 1.08x faster                                      |
| xml_etree_process       | 74.5 ms                                                | 68.9 ms: 1.08x faster                                     |
| chameleon               | 9.17 ms                                                | 8.49 ms: 1.08x faster                                     |
| unpickle_pure_python    | 302 us                                                 | 279 us: 1.08x faster                                      |
| sqlalchemy_imperative   | 21.5 ms                                                | 19.9 ms: 1.08x faster                                     |
| gunicorn                | 1.43 ms                                                | 1.33 ms: 1.08x faster                                     |
| telco                   | 6.73 ms                                                | 6.27 ms: 1.07x faster                                     |
| aiohttp                 | 1.34 ms                                                | 1.25 ms: 1.07x faster                                     |
| 2to3                    | 335 ms                                                 | 313 ms: 1.07x faster                                      |
| deepcopy_reduce         | 3.79 us                                                | 3.55 us: 1.07x faster                                     |
| dulwich_log             | 75.8 ms                                                | 71.2 ms: 1.07x faster                                     |
| raytrace                | 467 ms                                                 | 440 ms: 1.06x faster                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.93 ms: 1.06x faster                                     |
| genshi_text             | 30.6 ms                                                | 29.0 ms: 1.06x faster                                     |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.05x faster                                      |
| pprint_pformat          | 1.98 sec                                               | 1.88 sec: 1.05x faster                                    |
| sqlglot_transpile       | 2.43 ms                                                | 2.31 ms: 1.05x faster                                     |
| logging_format          | 8.85 us                                                | 8.42 us: 1.05x faster                                     |
| scimark_lu              | 161 ms                                                 | 153 ms: 1.05x faster                                      |
| genshi_xml              | 63.7 ms                                                | 60.6 ms: 1.05x faster                                     |
| sympy_integrate         | 24.0 ms                                                | 22.9 ms: 1.05x faster                                     |
| pickle_pure_python      | 452 us                                                 | 432 us: 1.05x faster                                      |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.04x faster                                      |
| tornado_http            | 128 ms                                                 | 123 ms: 1.04x faster                                      |
| pprint_safe_repr        | 953 ms                                                 | 914 ms: 1.04x faster                                      |
| pylint                  | 532 ms                                                 | 512 ms: 1.04x faster                                      |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.03x faster                                      |
| asyncio_tcp             | 914 ms                                                 | 885 ms: 1.03x faster                                      |
| sympy_str               | 325 ms                                                 | 316 ms: 1.03x faster                                      |
| docutils                | 3.18 sec                                               | 3.10 sec: 1.03x faster                                    |
| flaskblogging           | 8.27 ms                                                | 8.07 ms: 1.03x faster                                     |
| logging_simple          | 8.10 us                                                | 7.90 us: 1.02x faster                                     |
| async_tree_memoization  | 855 ms                                                 | 839 ms: 1.02x faster                                      |
| pickle_list             | 4.72 us                                                | 4.65 us: 1.02x faster                                     |
| pickle_dict             | 27.6 us                                                | 27.2 us: 1.01x faster                                     |
| unpickle_list           | 4.92 us                                                | 4.86 us: 1.01x faster                                     |
| sympy_sum               | 183 ms                                                 | 181 ms: 1.01x faster                                      |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 164 ms: 1.01x faster                                      |
| json_dumps              | 13.4 ms                                                | 13.4 ms: 1.01x faster                                     |
| thrift                  | 1.03 ms                                                | 1.03 ms: 1.00x faster                                     |
| python_startup_no_site  | 5.78 ms                                                | 5.80 ms: 1.00x slower                                     |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                      |
| regex_v8                | 25.0 ms                                                | 25.3 ms: 1.01x slower                                     |
| json_loads              | 28.7 us                                                | 29.0 us: 1.01x slower                                     |
| async_tree_none         | 711 ms                                                 | 724 ms: 1.02x slower                                      |
| sqlglot_optimize        | 65.2 ms                                                | 66.5 ms: 1.02x slower                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 970 ms: 1.02x slower                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.69 ms: 1.03x slower                                     |
| regex_effbot            | 3.19 ms                                                | 3.31 ms: 1.04x slower                                     |
| sqlglot_normalize       | 134 ms                                                 | 139 ms: 1.04x slower                                      |
| django_template         | 46.3 ms                                                | 48.4 ms: 1.04x slower                                     |
| python_startup          | 14.1 ms                                                | 15.2 ms: 1.08x slower                                     |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                     |
| logging_silent          | 176 ns                                                 | 194 ns: 1.10x slower                                      |
| async_generators        | 426 ms                                                 | 495 ms: 1.16x slower                                      |
| Geometric mean          | (ref)                                                  | 1.06x faster                                              |

Benchmark hidden because not significant (11): djangocms, deltablue, pickle, sympy_expand, mdp, bench_mp_pool, sqlite_synth, bench_thread_pool, json, pathlib, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage, dask, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220720-3.10.1-53f2d50/bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50.json: mypy
