
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 206f05a
- commit date: 2023-01-14
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 183 ms: 1.10x faster                                   |
| chameleon      | 5.79 ms                                                | 4.59 ms: 1.26x faster                                  |
| docutils       | 1.78 sec                                               | 1.44 sec: 1.23x faster                                 |
| html5lib       | 44.2 ms                                                | 34.7 ms: 1.27x faster                                  |
| tornado_http   | 91.5 ms                                                | 68.3 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.4 ms: 1.47x faster                                  |
| float          | 72.4 ms                                                | 51.5 ms: 1.41x faster                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 74.6 ms: 1.29x faster                                  |
| regex_dna      | 162 ms                                                 | 154 ms: 1.05x faster                                   |
| regex_v8       | 17.6 ms                                                | 16.8 ms: 1.04x faster                                  |
| regex_effbot   | 2.46 ms                                                | 2.73 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.12 ms: 1.37x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 34.8 ms: 1.29x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 93.1 ms: 1.14x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.0 ms: 1.13x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 66.4 ms: 1.09x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| unpickle_list        | 2.69 us                                                | 2.71 us: 1.01x slower                                  |
| pickle               | 7.35 us                                                | 7.56 us: 1.03x slower                                  |
| pickle_list          | 2.80 us                                                | 2.89 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.33 ms: 1.28x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 7.34 ms: 1.21x faster                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 37.2 ms                                                | 28.4 ms: 1.31x faster                                  |
| mako            | 10.5 ms                                                | 8.10 ms: 1.29x faster                                  |
| django_template | 27.3 ms                                                | 21.7 ms: 1.26x faster                                  |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                  |
| Geometric mean  | (ref)                                                  | 1.27x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.61 ms: 1.97x faster                                  |
| logging_silent          | 119 ns                                                 | 66.2 ns: 1.80x faster                                  |
| richards                | 51.4 ms                                                | 30.4 ms: 1.69x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 408 ms: 1.64x faster                                   |
| scimark_sor             | 126 ms                                                 | 82.0 ms: 1.54x faster                                  |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                   |
| scimark_lu              | 109 ms                                                 | 72.3 ms: 1.51x faster                                  |
| async_tree_memoization  | 490 ms                                                 | 327 ms: 1.50x faster                                   |
| crypto_pyaes            | 78.1 ms                                                | 52.9 ms: 1.48x faster                                  |
| nbody                   | 93.3 ms                                                | 63.4 ms: 1.47x faster                                  |
| pickle_pure_python      | 283 us                                                 | 194 us: 1.46x faster                                   |
| raytrace                | 325 ms                                                 | 223 ms: 1.46x faster                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 50.6 ms: 1.43x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                   |
| pyflate                 | 453 ms                                                 | 319 ms: 1.42x faster                                   |
| float                   | 72.4 ms                                                | 51.5 ms: 1.41x faster                                  |
| async_tree_none         | 400 ms                                                 | 285 ms: 1.41x faster                                   |
| async_tree_io           | 1.02 sec                                               | 737 ms: 1.38x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.9 ms: 1.38x faster                                  |
| json_dumps              | 8.40 ms                                                | 6.12 ms: 1.37x faster                                  |
| pycparser               | 916 ms                                                 | 682 ms: 1.34x faster                                   |
| tornado_http            | 91.5 ms                                                | 68.3 ms: 1.34x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.02 ms: 1.33x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 25.9 us: 1.33x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.18 ms: 1.33x faster                                  |
| chaos                   | 66.7 ms                                                | 50.3 ms: 1.33x faster                                  |
| logging_simple          | 4.63 us                                                | 3.50 us: 1.32x faster                                  |
| thrift                  | 580 us                                                 | 442 us: 1.31x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 939 ms: 1.31x faster                                   |
| logging_format          | 4.97 us                                                | 3.79 us: 1.31x faster                                  |
| genshi_xml              | 37.2 ms                                                | 28.4 ms: 1.31x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 464 ms: 1.30x faster                                   |
| spectral_norm           | 95.8 ms                                                | 73.6 ms: 1.30x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.6 ms: 1.30x faster                                  |
| mako                    | 10.5 ms                                                | 8.10 ms: 1.29x faster                                  |
| regex_compile           | 96.4 ms                                                | 74.6 ms: 1.29x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 34.8 ms: 1.29x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.92 ms: 1.28x faster                                  |
| python_startup          | 11.9 ms                                                | 9.33 ms: 1.28x faster                                  |
| deepcopy                | 281 us                                                 | 220 us: 1.27x faster                                   |
| create_gc_cycles        | 880 us                                                 | 690 us: 1.27x faster                                   |
| html5lib                | 44.2 ms                                                | 34.7 ms: 1.27x faster                                  |
| chameleon               | 5.79 ms                                                | 4.59 ms: 1.26x faster                                  |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.26x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.90 us: 1.25x faster                                  |
| fannkuch                | 317 ms                                                 | 255 ms: 1.24x faster                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.79 ms: 1.24x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 540 ms: 1.24x faster                                   |
| docutils                | 1.78 sec                                               | 1.44 sec: 1.23x faster                                 |
| bench_thread_pool       | 546 us                                                 | 447 us: 1.22x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.2 ms: 1.22x faster                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.34 ms: 1.21x faster                                  |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                  |
| scimark_fft             | 230 ms                                                 | 195 ms: 1.18x faster                                   |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.4 ms: 1.16x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 171 ms: 1.14x faster                                   |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.14x faster                                   |
| xml_etree_parse         | 106 ms                                                 | 93.1 ms: 1.14x faster                                  |
| unpack_sequence         | 37.4 ns                                                | 32.8 ns: 1.14x faster                                  |
| xml_etree_generate      | 54.2 ms                                                | 48.0 ms: 1.13x faster                                  |
| nqueens                 | 68.2 ms                                                | 60.8 ms: 1.12x faster                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                   |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                 |
| 2to3                    | 201 ms                                                 | 183 ms: 1.10x faster                                   |
| json                    | 3.08 ms                                                | 2.82 ms: 1.09x faster                                  |
| sympy_sum               | 93.6 ms                                                | 85.9 ms: 1.09x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 66.4 ms: 1.09x faster                                  |
| coroutines              | 20.2 ms                                                | 18.6 ms: 1.08x faster                                  |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.38 us: 1.07x faster                                  |
| regex_dna               | 162 ms                                                 | 154 ms: 1.05x faster                                   |
| meteor_contest          | 78.1 ms                                                | 74.5 ms: 1.05x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.8 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                  |
| unpickle_list           | 2.69 us                                                | 2.71 us: 1.01x slower                                  |
| generators              | 32.7 ms                                                | 33.6 ms: 1.03x slower                                  |
| pickle                  | 7.35 us                                                | 7.56 us: 1.03x slower                                  |
| pickle_list             | 2.80 us                                                | 2.89 us: 1.03x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 42.1 ms: 1.06x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.73 ms: 1.11x slower                                  |
| dask                    | 265 ms                                                 | 321 ms: 1.21x slower                                   |
| coverage                | 42.0 ms                                                | 56.4 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.23x faster                                           |

Benchmark hidden because not significant (2): unpickle, pidigits
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230114-3.12.0a4+-206f05a/bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a.json: mypy
