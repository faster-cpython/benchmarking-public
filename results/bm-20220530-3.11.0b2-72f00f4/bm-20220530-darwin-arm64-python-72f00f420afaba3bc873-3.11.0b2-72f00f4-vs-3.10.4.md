
# Results vs. 3.10.4

- fork: python
- ref: 72f00f420afaba3bc873
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.22x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 182 ms: 1.11x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.71 ms: 1.23x faster                                                 |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| html5lib       | 44.2 ms                                                | 35.9 ms: 1.23x faster                                                 |
| tornado_http   | 91.5 ms                                                | 69.6 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.9 ms: 1.46x faster                                                 |
| float          | 72.4 ms                                                | 55.0 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.4 ms: 1.24x faster                                                 |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| regex_v8       | 17.6 ms                                                | 16.6 ms: 1.06x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.39 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 44.8 ms                                                | 34.7 ms: 1.29x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 223 us: 1.27x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 175 us: 1.16x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 65.3 ms: 1.11x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.63 ms: 1.10x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.71 us: 1.04x faster                                                 |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| pickle               | 7.35 us                                                | 7.12 us: 1.03x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.15 ms: 1.30x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.20 ms: 1.23x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.0 ms: 1.30x faster                                                 |
| mako            | 10.5 ms                                                | 8.38 ms: 1.25x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.4 ms: 1.19x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 31.3 ms: 1.19x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 65.4 ns: 1.82x faster                                                 |
| deltablue               | 5.14 ms                                                | 2.84 ms: 1.81x faster                                                 |
| scimark_sor             | 126 ms                                                 | 75.5 ms: 1.67x faster                                                 |
| raytrace                | 325 ms                                                 | 210 ms: 1.55x faster                                                  |
| go                      | 165 ms                                                 | 108 ms: 1.54x faster                                                  |
| richards                | 51.4 ms                                                | 33.5 ms: 1.54x faster                                                 |
| scimark_lu              | 109 ms                                                 | 71.4 ms: 1.53x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 51.6 ms: 1.51x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 48.7 ms: 1.49x faster                                                 |
| nbody                   | 93.3 ms                                                | 63.9 ms: 1.46x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 702 ms: 1.45x faster                                                  |
| pyflate                 | 453 ms                                                 | 316 ms: 1.43x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 344 ms: 1.43x faster                                                  |
| async_tree_none         | 400 ms                                                 | 287 ms: 1.40x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.6 ms: 1.39x faster                                                 |
| chaos                   | 66.7 ms                                                | 49.4 ms: 1.35x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.70 ms: 1.35x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.46 us: 1.34x faster                                                 |
| thrift                  | 580 us                                                 | 437 us: 1.33x faster                                                  |
| logging_format          | 4.97 us                                                | 3.74 us: 1.33x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 72.2 ms: 1.33x faster                                                 |
| float                   | 72.4 ms                                                | 55.0 ms: 1.32x faster                                                 |
| tornado_http            | 91.5 ms                                                | 69.6 ms: 1.32x faster                                                 |
| pycparser               | 916 ms                                                 | 703 ms: 1.30x faster                                                  |
| python_startup          | 11.9 ms                                                | 9.15 ms: 1.30x faster                                                 |
| django_template         | 27.3 ms                                                | 21.0 ms: 1.30x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 34.7 ms: 1.29x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 223 us: 1.27x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.4 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 534 ms: 1.25x faster                                                  |
| mako                    | 10.5 ms                                                | 8.38 ms: 1.25x faster                                                 |
| regex_compile           | 96.4 ms                                                | 77.4 ms: 1.24x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 490 ms: 1.24x faster                                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.20 ms: 1.23x faster                                                 |
| html5lib                | 44.2 ms                                                | 35.9 ms: 1.23x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.71 ms: 1.23x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.23x faster                                                |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.26 ms: 1.22x faster                                                 |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| fannkuch                | 317 ms                                                 | 260 ms: 1.22x faster                                                  |
| sqlalchemy_declarative  | 74.9 ms                                                | 61.5 ms: 1.22x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                                 |
| aiohttp                 | 1.27 ms                                                | 1.05 ms: 1.21x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 28.5 us: 1.21x faster                                                 |
| gunicorn                | 1.35 ms                                                | 1.13 ms: 1.19x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.4 ms: 1.19x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 31.3 ms: 1.19x faster                                                 |
| generators              | 32.7 ms                                                | 27.6 ms: 1.19x faster                                                 |
| async_generators        | 234 ms                                                 | 198 ms: 1.18x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 462 us: 1.18x faster                                                  |
| deepcopy                | 281 us                                                 | 239 us: 1.18x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.35 ms: 1.17x faster                                                 |
| pylint                  | 307 ms                                                 | 263 ms: 1.17x faster                                                  |
| nqueens                 | 68.2 ms                                                | 58.7 ms: 1.16x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 175 us: 1.16x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.2 ns: 1.16x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.05 us: 1.16x faster                                                 |
| coroutines              | 20.2 ms                                                | 17.4 ms: 1.16x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 170 ms: 1.16x faster                                                  |
| scimark_fft             | 230 ms                                                 | 200 ms: 1.15x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.19 ms: 1.15x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.15x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 82.2 ms: 1.14x faster                                                 |
| sympy_expand            | 275 ms                                                 | 243 ms: 1.13x faster                                                  |
| sympy_str               | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                 |
| 2to3                    | 201 ms                                                 | 182 ms: 1.11x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 65.3 ms: 1.11x faster                                                 |
| json_dumps              | 8.40 ms                                                | 7.63 ms: 1.10x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.09x faster                                                |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.20 ms: 1.08x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| telco                   | 3.63 ms                                                | 3.41 ms: 1.06x faster                                                 |
| json                    | 3.08 ms                                                | 2.92 ms: 1.06x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.6 ms: 1.06x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| pickle_list             | 2.80 us                                                | 2.71 us: 1.04x faster                                                 |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| pickle                  | 7.35 us                                                | 7.12 us: 1.03x faster                                                 |
| regex_effbot            | 2.46 ms                                                | 2.39 ms: 1.03x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 77.4 ms: 1.01x faster                                                 |
| bench_mp_pool           | 39.7 ms                                                | 41.0 ms: 1.03x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (3): pidigits, unpickle, unpickle_list
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, flaskblogging, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220530-3.11.0b2-72f00f4/bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4.json: mypy
