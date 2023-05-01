
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 173 ms: 1.17x faster                                   |
| docutils       | 1.78 sec                                               | 1.56 sec: 1.14x faster                                 |
| html5lib       | 44.2 ms                                                | 37.2 ms: 1.19x faster                                  |
| tornado_http   | 91.5 ms                                                | 69.8 ms: 1.31x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 69.7 ms: 1.34x faster                                  |
| float          | 72.4 ms                                                | 58.1 ms: 1.25x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.6 ms: 1.24x faster                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| regex_v8       | 17.6 ms                                                | 16.3 ms: 1.08x faster                                  |
| regex_effbot   | 2.46 ms                                                | 2.69 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.34x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.84 ms: 1.23x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 39.8 ms: 1.12x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                   |
| xml_etree_iterparse  | 72.3 ms                                                | 74.2 ms: 1.03x slower                                  |
| unpickle             | 9.89 us                                                | 10.2 us: 1.03x slower                                  |
| json_loads           | 16.9 us                                                | 17.7 us: 1.05x slower                                  |
| pickle_dict          | 17.9 us                                                | 19.0 us: 1.06x slower                                  |
| pickle               | 7.35 us                                                | 7.83 us: 1.07x slower                                  |
| xml_etree_generate   | 54.2 ms                                                | 57.7 ms: 1.07x slower                                  |
| pickle_list          | 2.80 us                                                | 3.13 us: 1.12x slower                                  |
| unpickle_list        | 2.69 us                                                | 3.16 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.5 ms: 1.05x slower                                  |
| python_startup_no_site | 8.88 ms                                                | 10.4 ms: 1.17x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako           | 10.5 ms                                                | 7.80 ms: 1.34x faster                                  |
| genshi_text    | 18.4 ms                                                | 15.0 ms: 1.23x faster                                  |
| genshi_xml     | 37.2 ms                                                | 30.9 ms: 1.20x faster                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.47 ms: 2.08x faster                                  |
| logging_silent          | 119 ns                                                 | 70.8 ns: 1.69x faster                                  |
| richards                | 51.4 ms                                                | 31.6 ms: 1.63x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 897 us: 1.52x faster                                   |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                   |
| asyncio_tcp             | 670 ms                                                 | 449 ms: 1.49x faster                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.07 ms: 1.47x faster                                  |
| scimark_sor             | 126 ms                                                 | 86.0 ms: 1.47x faster                                  |
| async_tree_memoization  | 490 ms                                                 | 335 ms: 1.46x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.32 ms: 1.46x faster                                  |
| pickle_pure_python      | 283 us                                                 | 194 us: 1.46x faster                                   |
| async_tree_io           | 1.02 sec                                               | 710 ms: 1.44x faster                                   |
| async_tree_none         | 400 ms                                                 | 281 ms: 1.42x faster                                   |
| scimark_lu              | 109 ms                                                 | 77.3 ms: 1.41x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 51.5 ms: 1.41x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 56.0 ms: 1.40x faster                                  |
| chaos                   | 66.7 ms                                                | 48.4 ms: 1.38x faster                                  |
| mako                    | 10.5 ms                                                | 7.80 ms: 1.34x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 151 us: 1.34x faster                                   |
| nbody                   | 93.3 ms                                                | 69.7 ms: 1.34x faster                                  |
| unpack_sequence         | 37.4 ns                                                | 28.1 ns: 1.33x faster                                  |
| pyflate                 | 453 ms                                                 | 342 ms: 1.32x faster                                   |
| pycparser               | 916 ms                                                 | 696 ms: 1.32x faster                                   |
| raytrace                | 325 ms                                                 | 248 ms: 1.31x faster                                   |
| deepcopy_memo           | 34.4 us                                                | 26.2 us: 1.31x faster                                  |
| tornado_http            | 91.5 ms                                                | 69.8 ms: 1.31x faster                                  |
| generators              | 32.7 ms                                                | 25.0 ms: 1.31x faster                                  |
| create_gc_cycles        | 880 us                                                 | 698 us: 1.26x faster                                   |
| logging_simple          | 4.63 us                                                | 3.70 us: 1.25x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 534 ms: 1.25x faster                                   |
| logging_format          | 4.97 us                                                | 3.98 us: 1.25x faster                                  |
| float                   | 72.4 ms                                                | 58.1 ms: 1.25x faster                                  |
| regex_compile           | 96.4 ms                                                | 77.6 ms: 1.24x faster                                  |
| spectral_norm           | 95.8 ms                                                | 77.2 ms: 1.24x faster                                  |
| genshi_text             | 18.4 ms                                                | 15.0 ms: 1.23x faster                                  |
| json_dumps              | 8.40 ms                                                | 6.84 ms: 1.23x faster                                  |
| dulwich_log             | 37.1 ms                                                | 30.5 ms: 1.22x faster                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.33 ms: 1.21x faster                                  |
| pprint_pformat          | 1.23 sec                                               | 1.02 sec: 1.20x faster                                 |
| genshi_xml              | 37.2 ms                                                | 30.9 ms: 1.20x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 509 ms: 1.19x faster                                   |
| html5lib                | 44.2 ms                                                | 37.2 ms: 1.19x faster                                  |
| deepcopy                | 281 us                                                 | 238 us: 1.18x faster                                   |
| 2to3                    | 201 ms                                                 | 173 ms: 1.17x faster                                   |
| mypy2                   | 307 ms                                                 | 265 ms: 1.16x faster                                   |
| docutils                | 1.78 sec                                               | 1.56 sec: 1.14x faster                                 |
| fannkuch                | 317 ms                                                 | 278 ms: 1.14x faster                                   |
| thrift                  | 580 us                                                 | 513 us: 1.13x faster                                   |
| xml_etree_process       | 44.8 ms                                                | 39.8 ms: 1.12x faster                                  |
| coroutines              | 20.2 ms                                                | 18.0 ms: 1.12x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.13 us: 1.12x faster                                  |
| scimark_fft             | 230 ms                                                 | 207 ms: 1.12x faster                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 68.0 ms: 1.10x faster                                  |
| bench_thread_pool       | 546 us                                                 | 498 us: 1.10x faster                                   |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| regex_v8                | 17.6 ms                                                | 16.3 ms: 1.08x faster                                  |
| nqueens                 | 68.2 ms                                                | 63.5 ms: 1.07x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 35.8 ms: 1.06x faster                                  |
| mdp                     | 1.66 sec                                               | 1.57 sec: 1.06x faster                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.27 ms: 1.06x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                  |
| json                    | 3.08 ms                                                | 3.02 ms: 1.02x faster                                  |
| meteor_contest          | 78.1 ms                                                | 77.4 ms: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                   |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                  |
| xml_etree_parse         | 106 ms                                                 | 109 ms: 1.02x slower                                   |
| comprehensions          | 17.6 us                                                | 18.0 us: 1.02x slower                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 74.2 ms: 1.03x slower                                  |
| unpickle                | 9.89 us                                                | 10.2 us: 1.03x slower                                  |
| python_startup          | 11.9 ms                                                | 12.5 ms: 1.05x slower                                  |
| json_loads              | 16.9 us                                                | 17.7 us: 1.05x slower                                  |
| pickle_dict             | 17.9 us                                                | 19.0 us: 1.06x slower                                  |
| pickle                  | 7.35 us                                                | 7.83 us: 1.07x slower                                  |
| xml_etree_generate      | 54.2 ms                                                | 57.7 ms: 1.07x slower                                  |
| telco                   | 3.63 ms                                                | 3.92 ms: 1.08x slower                                  |
| sqlite_synth            | 1.47 us                                                | 1.59 us: 1.08x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.69 ms: 1.09x slower                                  |
| pickle_list             | 2.80 us                                                | 3.13 us: 1.12x slower                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.4 ms: 1.17x slower                                  |
| unpickle_list           | 2.69 us                                                | 3.16 us: 1.17x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 48.6 ms: 1.22x slower                                  |
| dask                    | 265 ms                                                 | 329 ms: 1.24x slower                                   |
| async_generators        | 234 ms                                                 | 311 ms: 1.33x slower                                   |
| coverage                | 42.0 ms                                                | 57.4 ms: 1.36x slower                                  |
| Geometric mean          | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (1): sqlglot_normalize
Ignored benchmarks (10) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
