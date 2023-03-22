
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: c1c5882
- commit date: 2023-01-21
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 183 ms: 1.10x faster                                   |
| chameleon      | 5.79 ms                                                | 4.60 ms: 1.26x faster                                  |
| docutils       | 1.78 sec                                               | 1.44 sec: 1.23x faster                                 |
| html5lib       | 44.2 ms                                                | 35.0 ms: 1.26x faster                                  |
| tornado_http   | 91.5 ms                                                | 69.1 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.5 ms: 1.47x faster                                  |
| float          | 72.4 ms                                                | 51.4 ms: 1.41x faster                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 73.4 ms: 1.31x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.2 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 192 us: 1.48x faster                                   |
| unpickle_pure_python | 203 us                                                 | 144 us: 1.41x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.05 ms: 1.39x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 35.4 ms: 1.27x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 49.2 ms: 1.10x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 101 ms: 1.05x faster                                   |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 69.8 ms: 1.04x faster                                  |
| unpickle             | 9.89 us                                                | 9.76 us: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle_list        | 2.69 us                                                | 2.71 us: 1.01x slower                                  |
| pickle               | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.37 ms: 1.27x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 7.36 ms: 1.21x faster                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 37.2 ms                                                | 28.7 ms: 1.29x faster                                  |
| mako            | 10.5 ms                                                | 8.14 ms: 1.29x faster                                  |
| django_template | 27.3 ms                                                | 21.8 ms: 1.25x faster                                  |
| genshi_text     | 18.4 ms                                                | 15.5 ms: 1.19x faster                                  |
| Geometric mean  | (ref)                                                  | 1.25x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.61 ms: 1.97x faster                                  |
| logging_silent          | 119 ns                                                 | 66.4 ns: 1.80x faster                                  |
| richards                | 51.4 ms                                                | 30.5 ms: 1.69x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 434 ms: 1.54x faster                                   |
| scimark_sor             | 126 ms                                                 | 81.8 ms: 1.54x faster                                  |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                   |
| scimark_lu              | 109 ms                                                 | 72.3 ms: 1.51x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 48.3 ms: 1.50x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 52.2 ms: 1.50x faster                                  |
| raytrace                | 325 ms                                                 | 217 ms: 1.50x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 328 ms: 1.50x faster                                   |
| pickle_pure_python      | 283 us                                                 | 192 us: 1.48x faster                                   |
| nbody                   | 93.3 ms                                                | 63.5 ms: 1.47x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 144 us: 1.41x faster                                   |
| pyflate                 | 453 ms                                                 | 322 ms: 1.41x faster                                   |
| float                   | 72.4 ms                                                | 51.4 ms: 1.41x faster                                  |
| async_tree_none         | 400 ms                                                 | 286 ms: 1.40x faster                                   |
| chaos                   | 66.7 ms                                                | 47.9 ms: 1.39x faster                                  |
| async_tree_io           | 1.02 sec                                               | 732 ms: 1.39x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.05 ms: 1.39x faster                                  |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.38x faster                                  |
| pycparser               | 916 ms                                                 | 679 ms: 1.35x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.73 ms: 1.34x faster                                  |
| tornado_http            | 91.5 ms                                                | 69.1 ms: 1.32x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 26.1 us: 1.32x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.04 ms: 1.32x faster                                  |
| thrift                  | 580 us                                                 | 441 us: 1.32x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 936 ms: 1.32x faster                                   |
| pprint_safe_repr        | 606 ms                                                 | 460 ms: 1.32x faster                                   |
| regex_compile           | 96.4 ms                                                | 73.4 ms: 1.31x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.20 ms: 1.31x faster                                  |
| logging_simple          | 4.63 us                                                | 3.55 us: 1.30x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.6 ms: 1.30x faster                                  |
| spectral_norm           | 95.8 ms                                                | 74.0 ms: 1.30x faster                                  |
| logging_format          | 4.97 us                                                | 3.84 us: 1.29x faster                                  |
| genshi_xml              | 37.2 ms                                                | 28.7 ms: 1.29x faster                                  |
| mako                    | 10.5 ms                                                | 8.14 ms: 1.29x faster                                  |
| python_startup          | 11.9 ms                                                | 9.37 ms: 1.27x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 35.4 ms: 1.27x faster                                  |
| deepcopy                | 281 us                                                 | 222 us: 1.27x faster                                   |
| html5lib                | 44.2 ms                                                | 35.0 ms: 1.26x faster                                  |
| create_gc_cycles        | 880 us                                                 | 699 us: 1.26x faster                                   |
| chameleon               | 5.79 ms                                                | 4.60 ms: 1.26x faster                                  |
| django_template         | 27.3 ms                                                | 21.8 ms: 1.25x faster                                  |
| fannkuch                | 317 ms                                                 | 254 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 538 ms: 1.24x faster                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.79 ms: 1.24x faster                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.92 us: 1.23x faster                                  |
| docutils                | 1.78 sec                                               | 1.44 sec: 1.23x faster                                 |
| bench_thread_pool       | 546 us                                                 | 447 us: 1.22x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.36 ms: 1.21x faster                                  |
| scimark_fft             | 230 ms                                                 | 192 ms: 1.20x faster                                   |
| genshi_text             | 18.4 ms                                                | 15.5 ms: 1.19x faster                                  |
| async_generators        | 234 ms                                                 | 197 ms: 1.19x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.4 ms: 1.16x faster                                  |
| sympy_expand            | 275 ms                                                 | 242 ms: 1.14x faster                                   |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 32.9 ns: 1.14x faster                                  |
| nqueens                 | 68.2 ms                                                | 60.0 ms: 1.14x faster                                  |
| sympy_str               | 169 ms                                                 | 152 ms: 1.12x faster                                   |
| xml_etree_generate      | 54.2 ms                                                | 49.2 ms: 1.10x faster                                  |
| 2to3                    | 201 ms                                                 | 183 ms: 1.10x faster                                   |
| mdp                     | 1.66 sec                                               | 1.51 sec: 1.10x faster                                 |
| sympy_sum               | 93.6 ms                                                | 85.4 ms: 1.10x faster                                  |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.2 ms: 1.09x faster                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| sqlite_synth            | 1.47 us                                                | 1.38 us: 1.07x faster                                  |
| coroutines              | 20.2 ms                                                | 18.9 ms: 1.06x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 101 ms: 1.05x faster                                   |
| telco                   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                  |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 69.8 ms: 1.04x faster                                  |
| meteor_contest          | 78.1 ms                                                | 75.5 ms: 1.03x faster                                  |
| unpickle                | 9.89 us                                                | 9.76 us: 1.01x faster                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle_list           | 2.69 us                                                | 2.71 us: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.52 us: 1.02x slower                                  |
| generators              | 32.7 ms                                                | 34.1 ms: 1.04x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.56 ms: 1.07x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 42.6 ms: 1.07x slower                                  |
| dask                    | 265 ms                                                 | 320 ms: 1.21x slower                                   |
| coverage                | 42.0 ms                                                | 55.5 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.23x faster                                           |

Benchmark hidden because not significant (2): pidigits, pickle_list
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230121-3.12.0a4+-c1c5882/bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882.json: mypy
