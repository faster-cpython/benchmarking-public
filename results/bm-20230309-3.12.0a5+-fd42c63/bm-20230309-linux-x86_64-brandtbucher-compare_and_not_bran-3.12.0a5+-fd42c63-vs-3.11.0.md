
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: fd42c63
- commit date: 2023-03-09
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.41 ms: 1.01x slower                                                        |
| docutils       | 2.60 sec                                               | 2.58 sec: 1.01x faster                                                       |
| html5lib       | 64.8 ms                                                | 62.8 ms: 1.03x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.7 ms: 1.03x faster                                                        |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| nbody          | 90.0 ms                                                | 93.9 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 203 ms                                                 | 199 ms: 1.02x faster                                                         |
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                        |
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                                         |
| regex_effbot   | 3.46 ms                                                | 3.53 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 207 us: 1.10x faster                                                         |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 290 us: 1.06x faster                                                         |
| pickle_list          | 4.14 us                                                | 4.07 us: 1.02x faster                                                        |
| pickle_dict          | 31.2 us                                                | 30.7 us: 1.01x faster                                                        |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                                        |
| xml_etree_process    | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                        |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 81.9 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.9 ms: 1.07x faster                                                        |
| django_template | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                        |
| mako            | 9.83 ms                                                | 10.2 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.9 ms: 2.37x faster                                                        |
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                        |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                         |
| deltablue               | 3.66 ms                                                | 3.28 ms: 1.12x faster                                                        |
| coroutines              | 26.2 ms                                                | 23.5 ms: 1.11x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 207 us: 1.10x faster                                                         |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| genshi_xml              | 51.4 ms                                                | 47.9 ms: 1.07x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 290 us: 1.06x faster                                                         |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                       |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                        |
| richards                | 46.1 ms                                                | 43.8 ms: 1.05x faster                                                        |
| scimark_sor             | 115 ms                                                 | 110 ms: 1.05x faster                                                         |
| unpack_sequence         | 44.5 ns                                                | 42.7 ns: 1.04x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                        |
| hexiom                  | 6.34 ms                                                | 6.10 ms: 1.04x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 73.1 ms: 1.04x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                       |
| html5lib                | 64.8 ms                                                | 62.8 ms: 1.03x faster                                                        |
| chaos                   | 68.7 ms                                                | 66.6 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                                         |
| coverage                | 99.3 ms                                                | 96.5 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| float                   | 76.8 ms                                                | 74.7 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| bench_thread_pool       | 817 us                                                 | 795 us: 1.03x faster                                                         |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 95.6 ms: 1.03x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.87 us: 1.03x faster                                                        |
| fannkuch                | 384 ms                                                 | 375 ms: 1.02x faster                                                         |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.02x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 35.0 us: 1.02x faster                                                        |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                                         |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| regex_dna               | 203 ms                                                 | 199 ms: 1.02x faster                                                         |
| tornado_http            | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.07 us: 1.02x faster                                                        |
| pyflate                 | 419 ms                                                 | 412 ms: 1.02x faster                                                         |
| raytrace                | 291 ms                                                 | 287 ms: 1.01x faster                                                         |
| deepcopy                | 341 us                                                 | 337 us: 1.01x faster                                                         |
| pickle_dict             | 31.2 us                                                | 30.7 us: 1.01x faster                                                        |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                                         |
| logging_format          | 6.48 us                                                | 6.41 us: 1.01x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                        |
| sympy_str               | 291 ms                                                 | 288 ms: 1.01x faster                                                         |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                                        |
| nqueens                 | 83.8 ms                                                | 82.9 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.99 us: 1.01x faster                                                        |
| mdp                     | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                       |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                       |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 63.5 ms: 1.01x faster                                                        |
| docutils                | 2.60 sec                                               | 2.58 sec: 1.01x faster                                                       |
| go                      | 140 ms                                                 | 140 ms: 1.00x faster                                                         |
| scimark_monte_carlo     | 68.0 ms                                                | 68.3 ms: 1.01x slower                                                        |
| chameleon               | 6.38 ms                                                | 6.41 ms: 1.01x slower                                                        |
| thrift                  | 760 us                                                 | 765 us: 1.01x slower                                                         |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.01x slower                                                         |
| sqlalchemy_declarative  | 138 ms                                                 | 140 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed | 736 ms                                                 | 745 ms: 1.01x slower                                                         |
| regex_effbot            | 3.46 ms                                                | 3.53 ms: 1.02x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                        |
| django_template         | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                        |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                        |
| mako                    | 9.83 ms                                                | 10.2 ms: 1.04x slower                                                        |
| nbody                   | 90.0 ms                                                | 93.9 ms: 1.04x slower                                                        |
| scimark_lu              | 108 ms                                                 | 113 ms: 1.05x slower                                                         |
| async_tree_memoization  | 624 ms                                                 | 655 ms: 1.05x slower                                                         |
| python_startup          | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.06x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.46 ms: 1.07x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 81.9 ms: 1.08x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                        |
| gc_traversal            | 3.82 ms                                                | 4.19 ms: 1.10x slower                                                        |
| async_generators        | 356 ms                                                 | 420 ms: 1.18x slower                                                         |
| dask                    | 365 ms                                                 | 513 ms: 1.40x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (12): logging_silent, async_tree_none, sqlalchemy_imperative, xml_etree_iterparse, djangocms, bench_mp_pool, telco, scimark_fft, meteor_contest, genshi_text, scimark_sparse_mat_mult, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230309-3.12.0a5+-fd42c63/bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63.json: comprehensions
