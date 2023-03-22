
# Results vs. 3.11.0

- fork: python
- ref: 14d4f68ebb495fe7ccba
- machine: darwin-arm64
- commit hash: 14d4f68
- commit date: 2022-10-02
- overall geometric mean: 1.01x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.69 ms: 1.02x slower                                                 |
| docutils       | 1.47 sec                                               | 1.47 sec: 1.00x slower                                                |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| float          | 53.0 ms                                                | 56.1 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.13 ms: 1.26x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 64.9 ms: 1.07x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.56 us: 1.03x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 47.6 ms: 1.02x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.02x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 205 us: 1.03x slower                                                  |
| pickle               | 7.17 us                                                | 7.55 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.16 ms: 1.30x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.06 ms: 1.27x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.14 ms: 1.04x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.3 ms: 1.02x slower                                                 |
| django_template | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.6 ms: 1.35x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.16 ms: 1.30x faster                                                 |
| python_startup          | 11.5 ms                                                | 9.06 ms: 1.27x faster                                                 |
| json_dumps              | 7.72 ms                                                | 6.13 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.82 ms: 1.13x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| coverage                | 58.6 ms                                                | 53.5 ms: 1.09x faster                                                 |
| flaskblogging           | 2.42 ms                                                | 2.23 ms: 1.08x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 64.9 ms: 1.07x faster                                                 |
| mako                    | 8.49 ms                                                | 8.14 ms: 1.04x faster                                                 |
| bench_thread_pool       | 473 us                                                 | 454 us: 1.04x faster                                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.06 ms: 1.04x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 41.9 ms: 1.03x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.56 us: 1.03x faster                                                 |
| dulwich_log             | 29.9 ms                                                | 29.1 ms: 1.03x faster                                                 |
| sqlalchemy_declarative  | 62.7 ms                                                | 61.2 ms: 1.02x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 47.6 ms: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna               | 152 ms                                                 | 150 ms: 1.01x faster                                                  |
| telco                   | 3.39 ms                                                | 3.36 ms: 1.01x faster                                                 |
| mdp                     | 1.54 sec                                               | 1.53 sec: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 534 ms                                                 | 530 ms: 1.01x faster                                                  |
| xml_etree_process       | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                 |
| async_tree_none         | 285 ms                                                 | 283 ms: 1.01x faster                                                  |
| scimark_fft             | 199 ms                                                 | 199 ms: 1.00x faster                                                  |
| docutils                | 1.47 sec                                               | 1.47 sec: 1.00x slower                                                |
| spectral_norm           | 72.8 ms                                                | 73.0 ms: 1.00x slower                                                 |
| scimark_lu              | 72.1 ms                                                | 72.3 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| genshi_text             | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.83 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| sympy_str               | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.2 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| unpack_sequence         | 33.6 ns                                                | 34.1 ns: 1.02x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.02x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.3 ms: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                                 |
| sympy_expand            | 243 ms                                                 | 248 ms: 1.02x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 162 us: 1.02x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.9 ms: 1.02x slower                                                 |
| pycparser               | 697 ms                                                 | 713 ms: 1.02x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.69 ms: 1.02x slower                                                 |
| thrift                  | 433 us                                                 | 446 us: 1.03x slower                                                  |
| chaos                   | 49.5 ms                                                | 50.9 ms: 1.03x slower                                                 |
| async_generators        | 195 ms                                                 | 201 ms: 1.03x slower                                                  |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| richards                | 32.2 ms                                                | 33.2 ms: 1.03x slower                                                 |
| pickle_pure_python      | 199 us                                                 | 205 us: 1.03x slower                                                  |
| fannkuch                | 261 ms                                                 | 270 ms: 1.03x slower                                                  |
| async_tree_io           | 706 ms                                                 | 732 ms: 1.04x slower                                                  |
| django_template         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                 |
| raytrace                | 207 ms                                                 | 216 ms: 1.04x slower                                                  |
| hexiom                  | 4.73 ms                                                | 4.93 ms: 1.04x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.00 ms: 1.05x slower                                                 |
| logging_simple          | 3.50 us                                                | 3.68 us: 1.05x slower                                                 |
| logging_format          | 3.78 us                                                | 3.97 us: 1.05x slower                                                 |
| logging_silent          | 68.0 ns                                                | 71.7 ns: 1.05x slower                                                 |
| pickle                  | 7.17 us                                                | 7.55 us: 1.05x slower                                                 |
| meteor_contest          | 73.8 ms                                                | 78.1 ms: 1.06x slower                                                 |
| pprint_pformat          | 950 ms                                                 | 1.01 sec: 1.06x slower                                                |
| float                   | 53.0 ms                                                | 56.1 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 496 ms: 1.07x slower                                                  |
| deepcopy                | 224 us                                                 | 240 us: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.06 us: 1.08x slower                                                 |
| go                      | 109 ms                                                 | 118 ms: 1.08x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 28.5 us: 1.08x slower                                                 |
| coroutines              | 17.7 ms                                                | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 311 ms                                                 | 353 ms: 1.13x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 383 ms: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.46 us: 1.15x slower                                                 |
| scimark_monte_carlo     | 46.4 ms                                                | 55.4 ms: 1.19x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 101 ms: 1.21x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (6): tornado_http, pylint, nqueens, nbody, sympy_sum, unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221002-3.12.0a0-14d4f68/bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68.json: mypy
