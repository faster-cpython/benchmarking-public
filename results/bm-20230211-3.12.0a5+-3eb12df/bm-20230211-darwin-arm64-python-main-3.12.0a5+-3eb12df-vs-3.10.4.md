
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 181 ms: 1.11x faster                                   |
| chameleon      | 5.79 ms                                                | 4.34 ms: 1.33x faster                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.21x faster                                 |
| html5lib       | 44.2 ms                                                | 35.0 ms: 1.26x faster                                  |
| tornado_http   | 91.5 ms                                                | 68.4 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.1 ms: 1.48x faster                                  |
| float          | 72.4 ms                                                | 49.7 ms: 1.46x faster                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 71.0 ms: 1.36x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.0 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 150 ms: 1.08x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 185 us: 1.53x faster                                   |
| unpickle_pure_python | 203 us                                                 | 137 us: 1.48x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.06 ms: 1.39x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 35.2 ms: 1.27x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 93.0 ms: 1.14x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 49.2 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 67.1 ms: 1.08x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                  |
| pickle               | 7.35 us                                                | 7.57 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.36 ms: 1.27x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 7.38 ms: 1.20x faster                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.13 ms: 1.47x faster                                  |
| genshi_xml      | 37.2 ms                                                | 27.5 ms: 1.35x faster                                  |
| genshi_text     | 18.4 ms                                                | 13.8 ms: 1.33x faster                                  |
| django_template | 27.3 ms                                                | 20.8 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.47 ms: 2.08x faster                                  |
| logging_silent          | 119 ns                                                 | 64.1 ns: 1.86x faster                                  |
| richards                | 51.4 ms                                                | 29.5 ms: 1.74x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 411 ms: 1.63x faster                                   |
| scimark_lu              | 109 ms                                                 | 70.5 ms: 1.55x faster                                  |
| go                      | 165 ms                                                 | 107 ms: 1.55x faster                                   |
| pickle_pure_python      | 283 us                                                 | 185 us: 1.53x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 320 ms: 1.53x faster                                   |
| scimark_sor             | 126 ms                                                 | 83.4 ms: 1.51x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.21 ms: 1.50x faster                                  |
| raytrace                | 325 ms                                                 | 217 ms: 1.50x faster                                   |
| unpickle_pure_python    | 203 us                                                 | 137 us: 1.48x faster                                   |
| nbody                   | 93.3 ms                                                | 63.1 ms: 1.48x faster                                  |
| mako                    | 10.5 ms                                                | 7.13 ms: 1.47x faster                                  |
| chaos                   | 66.7 ms                                                | 45.5 ms: 1.47x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.4 ms: 1.46x faster                                  |
| float                   | 72.4 ms                                                | 49.7 ms: 1.46x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 50.0 ms: 1.45x faster                                  |
| async_tree_none         | 400 ms                                                 | 278 ms: 1.44x faster                                   |
| async_tree_io           | 1.02 sec                                               | 726 ms: 1.40x faster                                   |
| pyflate                 | 453 ms                                                 | 324 ms: 1.40x faster                                   |
| deepcopy_memo           | 34.4 us                                                | 24.7 us: 1.39x faster                                  |
| json_dumps              | 8.40 ms                                                | 6.06 ms: 1.39x faster                                  |
| pycparser               | 916 ms                                                 | 664 ms: 1.38x faster                                   |
| regex_compile           | 96.4 ms                                                | 71.0 ms: 1.36x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.01 ms: 1.35x faster                                  |
| genshi_xml              | 37.2 ms                                                | 27.5 ms: 1.35x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 452 ms: 1.34x faster                                   |
| pprint_pformat          | 1.23 sec                                               | 920 ms: 1.34x faster                                   |
| tornado_http            | 91.5 ms                                                | 68.4 ms: 1.34x faster                                  |
| chameleon               | 5.79 ms                                                | 4.34 ms: 1.33x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.18 ms: 1.33x faster                                  |
| genshi_text             | 18.4 ms                                                | 13.8 ms: 1.33x faster                                  |
| pathlib                 | 28.8 ms                                                | 21.8 ms: 1.32x faster                                  |
| logging_simple          | 4.63 us                                                | 3.51 us: 1.32x faster                                  |
| django_template         | 27.3 ms                                                | 20.8 ms: 1.31x faster                                  |
| deepcopy                | 281 us                                                 | 215 us: 1.31x faster                                   |
| logging_format          | 4.97 us                                                | 3.80 us: 1.31x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.4 ms: 1.31x faster                                  |
| spectral_norm           | 95.8 ms                                                | 73.4 ms: 1.31x faster                                  |
| thrift                  | 580 us                                                 | 447 us: 1.30x faster                                   |
| create_gc_cycles        | 880 us                                                 | 687 us: 1.28x faster                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.86 us: 1.28x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 35.2 ms: 1.27x faster                                  |
| python_startup          | 11.9 ms                                                | 9.36 ms: 1.27x faster                                  |
| fannkuch                | 317 ms                                                 | 251 ms: 1.26x faster                                   |
| html5lib                | 44.2 ms                                                | 35.0 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 534 ms: 1.25x faster                                   |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.12 ms: 1.25x faster                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.77 ms: 1.25x faster                                  |
| bench_thread_pool       | 546 us                                                 | 444 us: 1.23x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 30.6 ns: 1.22x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.1 ms: 1.22x faster                                  |
| scimark_fft             | 230 ms                                                 | 189 ms: 1.22x faster                                   |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.21x faster                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.38 ms: 1.20x faster                                  |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.7 ms: 1.20x faster                                  |
| sympy_integrate         | 13.3 ms                                                | 11.1 ms: 1.19x faster                                  |
| sympy_str               | 169 ms                                                 | 144 ms: 1.17x faster                                   |
| sqlglot_normalize       | 196 ms                                                 | 169 ms: 1.16x faster                                   |
| sympy_expand            | 275 ms                                                 | 238 ms: 1.16x faster                                   |
| nqueens                 | 68.2 ms                                                | 59.5 ms: 1.15x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 93.0 ms: 1.14x faster                                  |
| sympy_sum               | 93.6 ms                                                | 82.1 ms: 1.14x faster                                  |
| mypy2                   | 307 ms                                                 | 271 ms: 1.13x faster                                   |
| 2to3                    | 201 ms                                                 | 181 ms: 1.11x faster                                   |
| xml_etree_generate      | 54.2 ms                                                | 49.2 ms: 1.10x faster                                  |
| mdp                     | 1.66 sec                                               | 1.51 sec: 1.10x faster                                 |
| coroutines              | 20.2 ms                                                | 18.4 ms: 1.10x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.0 ms: 1.09x faster                                  |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                  |
| regex_dna               | 162 ms                                                 | 150 ms: 1.08x faster                                   |
| sqlite_synth            | 1.47 us                                                | 1.37 us: 1.08x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 67.1 ms: 1.08x faster                                  |
| meteor_contest          | 78.1 ms                                                | 72.7 ms: 1.07x faster                                  |
| telco                   | 3.63 ms                                                | 3.38 ms: 1.07x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| generators              | 32.7 ms                                                | 32.9 ms: 1.00x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.00x slower                                  |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.57 us: 1.03x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.60 ms: 1.06x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 42.6 ms: 1.07x slower                                  |
| async_generators        | 234 ms                                                 | 255 ms: 1.09x slower                                   |
| coverage                | 42.0 ms                                                | 60.3 ms: 1.43x slower                                  |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, dask, flaskblogging, gunicorn, pylint
