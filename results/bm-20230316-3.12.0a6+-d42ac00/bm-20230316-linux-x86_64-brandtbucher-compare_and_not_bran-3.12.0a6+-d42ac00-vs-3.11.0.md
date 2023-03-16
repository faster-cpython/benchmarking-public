
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: d42ac00
- commit date: 2023-03-16
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.52 ms: 1.02x slower                                                        |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                       |
| html5lib       | 64.8 ms                                                | 62.0 ms: 1.05x faster                                                        |
| tornado_http   | 96.5 ms                                                | 91.9 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                        |
| nbody          | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                        |
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                        |
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                                         |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                                         |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 289 us: 1.07x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                         |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.16 us: 1.01x slower                                                        |
| xml_etree_process    | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                        |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 80.3 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.91 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.7 ms: 1.08x faster                                                        |
| mako            | 9.83 ms                                                | 9.95 ms: 1.01x slower                                                        |
| django_template | 32.3 ms                                                | 33.4 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                                        |
| asyncio_tcp             | 883 ms                                                 | 506 ms: 1.74x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                        |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                         |
| coroutines              | 26.2 ms                                                | 22.9 ms: 1.14x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 203 us: 1.12x faster                                                         |
| spectral_norm           | 98.1 ms                                                | 90.0 ms: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| genshi_xml              | 51.4 ms                                                | 47.7 ms: 1.08x faster                                                        |
| richards                | 46.1 ms                                                | 43.0 ms: 1.07x faster                                                        |
| json_loads              | 26.1 us                                                | 24.4 us: 1.07x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 289 us: 1.07x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.47 sec: 1.06x faster                                                       |
| json                    | 4.87 ms                                                | 4.62 ms: 1.05x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                        |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.05x faster                                                         |
| unpack_sequence         | 44.5 ns                                                | 42.3 ns: 1.05x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.73 us: 1.05x faster                                                        |
| tornado_http            | 96.5 ms                                                | 91.9 ms: 1.05x faster                                                        |
| scimark_fft             | 325 ms                                                 | 311 ms: 1.05x faster                                                         |
| html5lib                | 64.8 ms                                                | 62.0 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                         |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                                         |
| gc_traversal            | 3.82 ms                                                | 3.66 ms: 1.04x faster                                                        |
| float                   | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.41 ms: 1.04x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                       |
| hexiom                  | 6.34 ms                                                | 6.11 ms: 1.04x faster                                                        |
| nqueens                 | 83.8 ms                                                | 80.9 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                                        |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                         |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| bench_thread_pool       | 817 us                                                 | 793 us: 1.03x faster                                                         |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                        |
| logging_silent          | 98.0 ns                                                | 95.2 ns: 1.03x faster                                                        |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                        |
| nbody                   | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 73.9 ms: 1.02x faster                                                        |
| logging_format          | 6.48 us                                                | 6.32 us: 1.02x faster                                                        |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                         |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                       |
| async_tree_none         | 526 ms                                                 | 515 ms: 1.02x faster                                                         |
| coverage                | 99.3 ms                                                | 97.2 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 691 ms: 1.02x faster                                                         |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.02x faster                                                       |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                        |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                        |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                         |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                         |
| pycparser               | 1.19 sec                                               | 1.17 sec: 1.01x faster                                                       |
| raytrace                | 291 ms                                                 | 289 ms: 1.01x faster                                                         |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                                         |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 67.5 ms: 1.01x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.16 us: 1.01x slower                                                        |
| scimark_lu              | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| mako                    | 9.83 ms                                                | 9.95 ms: 1.01x slower                                                        |
| telco                   | 6.43 ms                                                | 6.52 ms: 1.01x slower                                                        |
| pyflate                 | 419 ms                                                 | 425 ms: 1.02x slower                                                         |
| chameleon               | 6.38 ms                                                | 6.52 ms: 1.02x slower                                                        |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                         |
| thrift                  | 760 us                                                 | 780 us: 1.03x slower                                                         |
| django_template         | 32.3 ms                                                | 33.4 ms: 1.03x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                        |
| async_tree_memoization  | 624 ms                                                 | 648 ms: 1.04x slower                                                         |
| python_startup          | 8.58 ms                                                | 8.91 ms: 1.04x slower                                                        |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 80.3 ms: 1.06x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.65 us: 1.07x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                        |
| async_generators        | 356 ms                                                 | 414 ms: 1.16x slower                                                         |
| dask                    | 365 ms                                                 | 510 ms: 1.40x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (12): djangocms, fannkuch, meteor_contest, async_tree_cpu_io_mixed, dulwich_log, regex_effbot, sympy_sum, chaos, bench_mp_pool, unpickle_list, genshi_text, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-d42ac00/bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00.json: comprehensions
