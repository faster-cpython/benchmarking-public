
# Results vs. 3.11.0

- fork: mdboom
- ref: RegCPython
- machine: linux-x86_64
- commit hash: 53f2d50
- commit date: 2022-07-20
- overall geometric mean: 1.19x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 313 ms: 1.21x slower                                      |
| chameleon      | 6.38 ms                                                | 8.49 ms: 1.33x slower                                     |
| docutils       | 2.60 sec                                               | 3.10 sec: 1.19x slower                                    |
| html5lib       | 64.8 ms                                                | 76.8 ms: 1.19x slower                                     |
| tornado_http   | 96.5 ms                                                | 123 ms: 1.27x slower                                      |
| Geometric mean | (ref)                                                  | 1.24x slower                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                      |
| nbody          | 90.0 ms                                                | 101 ms: 1.12x slower                                      |
| float          | 76.8 ms                                                | 94.9 ms: 1.24x slower                                     |
| Geometric mean | (ref)                                                  | 1.10x slower                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.31 ms: 1.04x faster                                     |
| regex_dna      | 203 ms                                                 | 216 ms: 1.06x slower                                      |
| regex_v8       | 22.2 ms                                                | 25.3 ms: 1.14x slower                                     |
| regex_compile  | 136 ms                                                 | 157 ms: 1.15x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 27.2 us: 1.14x faster                                     |
| unpickle_list        | 4.99 us                                                | 4.86 us: 1.03x faster                                     |
| xml_etree_parse      | 160 ms                                                 | 158 ms: 1.02x faster                                      |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                     |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                      |
| unpickle             | 13.3 us                                                | 14.3 us: 1.08x slower                                     |
| json_dumps           | 12.4 ms                                                | 13.4 ms: 1.08x slower                                     |
| json_loads           | 26.1 us                                                | 29.0 us: 1.11x slower                                     |
| pickle_list          | 4.14 us                                                | 4.65 us: 1.12x slower                                     |
| xml_etree_generate   | 75.9 ms                                                | 86.2 ms: 1.14x slower                                     |
| unpickle_pure_python | 227 us                                                 | 279 us: 1.23x slower                                      |
| xml_etree_process    | 53.7 ms                                                | 68.9 ms: 1.28x slower                                     |
| pickle_pure_python   | 308 us                                                 | 432 us: 1.40x slower                                      |
| Geometric mean       | (ref)                                                  | 1.09x slower                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 5.80 ms: 1.04x faster                                     |
| python_startup         | 8.58 ms                                                | 15.2 ms: 1.77x slower                                     |
| Geometric mean         | (ref)                                                  | 1.30x slower                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 60.6 ms: 1.18x slower                                     |
| mako            | 9.83 ms                                                | 13.1 ms: 1.33x slower                                     |
| genshi_text     | 21.5 ms                                                | 29.0 ms: 1.35x slower                                     |
| django_template | 32.3 ms                                                | 48.4 ms: 1.50x slower                                     |
| Geometric mean  | (ref)                                                  | 1.33x slower                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| generators              | 73.5 ms                                                | 56.3 ms: 1.31x faster                                     |
| pickle_dict             | 31.2 us                                                | 27.2 us: 1.14x faster                                     |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.29 ms: 1.07x faster                                     |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                      |
| regex_effbot            | 3.46 ms                                                | 3.31 ms: 1.04x faster                                     |
| python_startup_no_site  | 6.04 ms                                                | 5.80 ms: 1.04x faster                                     |
| fannkuch                | 384 ms                                                 | 369 ms: 1.04x faster                                      |
| unpickle_list           | 4.99 us                                                | 4.86 us: 1.03x faster                                     |
| telco                   | 6.43 ms                                                | 6.27 ms: 1.03x faster                                     |
| xml_etree_parse         | 160 ms                                                 | 158 ms: 1.02x faster                                      |
| gc_traversal            | 3.82 ms                                                | 3.83 ms: 1.00x slower                                     |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                     |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                      |
| meteor_contest          | 104 ms                                                 | 108 ms: 1.04x slower                                      |
| scimark_fft             | 325 ms                                                 | 337 ms: 1.04x slower                                      |
| mdp                     | 2.63 sec                                               | 2.74 sec: 1.04x slower                                    |
| nqueens                 | 83.8 ms                                                | 88.6 ms: 1.06x slower                                     |
| regex_dna               | 203 ms                                                 | 216 ms: 1.06x slower                                      |
| unpickle                | 13.3 us                                                | 14.3 us: 1.08x slower                                     |
| json_dumps              | 12.4 ms                                                | 13.4 ms: 1.08x slower                                     |
| sympy_str               | 291 ms                                                 | 316 ms: 1.09x slower                                      |
| sympy_sum               | 166 ms                                                 | 181 ms: 1.09x slower                                      |
| coroutines              | 26.2 ms                                                | 28.6 ms: 1.09x slower                                     |
| sympy_integrate         | 21.0 ms                                                | 22.9 ms: 1.10x slower                                     |
| sqlalchemy_imperative   | 18.1 ms                                                | 19.9 ms: 1.10x slower                                     |
| json                    | 4.87 ms                                                | 5.37 ms: 1.10x slower                                     |
| pylint                  | 462 ms                                                 | 512 ms: 1.11x slower                                      |
| pathlib                 | 18.1 ms                                                | 20.1 ms: 1.11x slower                                     |
| djangocms               | 32.5 us                                                | 36.2 us: 1.11x slower                                     |
| dulwich_log             | 64.0 ms                                                | 71.2 ms: 1.11x slower                                     |
| json_loads              | 26.1 us                                                | 29.0 us: 1.11x slower                                     |
| create_gc_cycles        | 1.52 ms                                                | 1.69 ms: 1.12x slower                                     |
| sympy_expand            | 475 ms                                                 | 533 ms: 1.12x slower                                      |
| pickle_list             | 4.14 us                                                | 4.65 us: 1.12x slower                                     |
| nbody                   | 90.0 ms                                                | 101 ms: 1.12x slower                                      |
| flaskblogging           | 7.11 ms                                                | 8.07 ms: 1.13x slower                                     |
| xml_etree_generate      | 75.9 ms                                                | 86.2 ms: 1.14x slower                                     |
| regex_v8                | 22.2 ms                                                | 25.3 ms: 1.14x slower                                     |
| regex_compile           | 136 ms                                                 | 157 ms: 1.15x slower                                      |
| pycparser               | 1.19 sec                                               | 1.37 sec: 1.15x slower                                    |
| bench_thread_pool       | 817 us                                                 | 947 us: 1.16x slower                                      |
| deepcopy_reduce         | 3.02 us                                                | 3.55 us: 1.18x slower                                     |
| genshi_xml              | 51.4 ms                                                | 60.6 ms: 1.18x slower                                     |
| sqlite_synth            | 2.48 us                                                | 2.93 us: 1.18x slower                                     |
| deepcopy                | 341 us                                                 | 404 us: 1.18x slower                                      |
| sqlalchemy_declarative  | 138 ms                                                 | 164 ms: 1.18x slower                                      |
| html5lib                | 64.8 ms                                                | 76.8 ms: 1.19x slower                                     |
| unpack_sequence         | 44.5 ns                                                | 52.8 ns: 1.19x slower                                     |
| gunicorn                | 1.12 ms                                                | 1.33 ms: 1.19x slower                                     |
| docutils                | 2.60 sec                                               | 3.10 sec: 1.19x slower                                    |
| aiohttp                 | 1.05 ms                                                | 1.25 ms: 1.19x slower                                     |
| 2to3                    | 259 ms                                                 | 313 ms: 1.21x slower                                      |
| unpickle_pure_python    | 227 us                                                 | 279 us: 1.23x slower                                      |
| float                   | 76.8 ms                                                | 94.9 ms: 1.24x slower                                     |
| async_tree_io           | 1.30 sec                                               | 1.61 sec: 1.24x slower                                    |
| deepcopy_memo           | 35.8 us                                                | 45.1 us: 1.26x slower                                     |
| scimark_monte_carlo     | 68.0 ms                                                | 85.8 ms: 1.26x slower                                     |
| sqlglot_optimize        | 52.7 ms                                                | 66.5 ms: 1.26x slower                                     |
| spectral_norm           | 98.1 ms                                                | 124 ms: 1.26x slower                                      |
| tornado_http            | 96.5 ms                                                | 123 ms: 1.27x slower                                      |
| xml_etree_process       | 53.7 ms                                                | 68.9 ms: 1.28x slower                                     |
| pprint_pformat          | 1.46 sec                                               | 1.88 sec: 1.29x slower                                    |
| pprint_safe_repr        | 706 ms                                                 | 914 ms: 1.30x slower                                      |
| sqlglot_normalize       | 108 ms                                                 | 139 ms: 1.30x slower                                      |
| logging_format          | 6.48 us                                                | 8.42 us: 1.30x slower                                     |
| logging_simple          | 6.02 us                                                | 7.90 us: 1.31x slower                                     |
| async_tree_cpu_io_mixed | 736 ms                                                 | 970 ms: 1.32x slower                                      |
| chaos                   | 68.7 ms                                                | 91.1 ms: 1.33x slower                                     |
| hexiom                  | 6.34 ms                                                | 8.43 ms: 1.33x slower                                     |
| chameleon               | 6.38 ms                                                | 8.49 ms: 1.33x slower                                     |
| mako                    | 9.83 ms                                                | 13.1 ms: 1.33x slower                                     |
| async_tree_memoization  | 624 ms                                                 | 839 ms: 1.34x slower                                      |
| genshi_text             | 21.5 ms                                                | 29.0 ms: 1.35x slower                                     |
| thrift                  | 760 us                                                 | 1.03 ms: 1.36x slower                                     |
| async_tree_none         | 526 ms                                                 | 724 ms: 1.38x slower                                      |
| pyflate                 | 419 ms                                                 | 580 ms: 1.39x slower                                      |
| async_generators        | 356 ms                                                 | 495 ms: 1.39x slower                                      |
| sqlglot_transpile       | 1.65 ms                                                | 2.31 ms: 1.40x slower                                     |
| crypto_pyaes            | 75.7 ms                                                | 106 ms: 1.40x slower                                      |
| pickle_pure_python      | 308 us                                                 | 432 us: 1.40x slower                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.93 ms: 1.42x slower                                     |
| scimark_lu              | 108 ms                                                 | 153 ms: 1.42x slower                                      |
| go                      | 140 ms                                                 | 203 ms: 1.44x slower                                      |
| richards                | 46.1 ms                                                | 67.6 ms: 1.46x slower                                     |
| django_template         | 32.3 ms                                                | 48.4 ms: 1.50x slower                                     |
| raytrace                | 291 ms                                                 | 440 ms: 1.51x slower                                      |
| scimark_sor             | 115 ms                                                 | 176 ms: 1.53x slower                                      |
| python_startup          | 8.58 ms                                                | 15.2 ms: 1.77x slower                                     |
| logging_silent          | 98.0 ns                                                | 194 ns: 1.98x slower                                      |
| deltablue               | 3.66 ms                                                | 7.24 ms: 1.98x slower                                     |
| Geometric mean          | (ref)                                                  | 1.19x slower                                              |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_tcp
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: coverage, dask, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220720-3.10.1-53f2d50/bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50.json: mypy
