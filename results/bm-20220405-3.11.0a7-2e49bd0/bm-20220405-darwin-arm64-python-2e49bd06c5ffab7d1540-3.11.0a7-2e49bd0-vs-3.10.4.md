
# Results vs. 3.10.4

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 181 ms: 1.11x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.70 ms: 1.23x faster                                                 |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                |
| html5lib       | 44.2 ms                                                | 34.0 ms: 1.30x faster                                                 |
| tornado_http   | 91.5 ms                                                | 70.4 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.6 ms: 1.42x faster                                                 |
| float          | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.6 ms: 1.27x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.20 ms: 1.12x faster                                                 |
| regex_dna      | 162 ms                                                 | 169 ms: 1.05x slower                                                  |
| regex_v8       | 17.6 ms                                                | 20.5 ms: 1.17x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 200 us: 1.42x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 157 us: 1.29x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.1 ms: 1.28x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 47.9 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 64.4 ms: 1.12x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.58 ms: 1.11x faster                                                 |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.62 us: 1.02x faster                                                 |
| pickle               | 7.35 us                                                | 7.18 us: 1.02x faster                                                 |
| pickle_dict          | 17.9 us                                                | 19.2 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.13 ms: 1.30x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.18 ms: 1.24x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                 |
| mako            | 10.5 ms                                                | 8.21 ms: 1.28x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 31.4 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.67 ms: 1.93x faster                                                 |
| logging_silent          | 119 ns                                                 | 69.4 ns: 1.72x faster                                                 |
| richards                | 51.4 ms                                                | 32.1 ms: 1.60x faster                                                 |
| raytrace                | 325 ms                                                 | 209 ms: 1.56x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 316 ms: 1.55x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 46.9 ms: 1.54x faster                                                 |
| go                      | 165 ms                                                 | 107 ms: 1.54x faster                                                  |
| scimark_lu              | 109 ms                                                 | 72.6 ms: 1.50x faster                                                 |
| scimark_sor             | 126 ms                                                 | 84.7 ms: 1.49x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 693 ms: 1.47x faster                                                  |
| pyflate                 | 453 ms                                                 | 317 ms: 1.43x faster                                                  |
| async_tree_none         | 400 ms                                                 | 280 ms: 1.43x faster                                                  |
| nbody                   | 93.3 ms                                                | 65.6 ms: 1.42x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 200 us: 1.42x faster                                                  |
| float                   | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 56.5 ms: 1.38x faster                                                 |
| pathlib                 | 28.8 ms                                                | 20.9 ms: 1.38x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.38 us: 1.37x faster                                                 |
| logging_format          | 4.97 us                                                | 3.65 us: 1.36x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 25.4 us: 1.36x faster                                                 |
| chaos                   | 66.7 ms                                                | 49.7 ms: 1.34x faster                                                 |
| thrift                  | 580 us                                                 | 439 us: 1.32x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 460 ms: 1.32x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 940 ms: 1.31x faster                                                  |
| python_startup          | 11.9 ms                                                | 9.13 ms: 1.30x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 73.6 ms: 1.30x faster                                                 |
| html5lib                | 44.2 ms                                                | 34.0 ms: 1.30x faster                                                 |
| tornado_http            | 91.5 ms                                                | 70.4 ms: 1.30x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.87 ms: 1.30x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 157 us: 1.29x faster                                                  |
| django_template         | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                 |
| deepcopy                | 281 us                                                 | 220 us: 1.28x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 35.1 ms: 1.28x faster                                                 |
| mako                    | 10.5 ms                                                | 8.21 ms: 1.28x faster                                                 |
| regex_compile           | 96.4 ms                                                | 75.6 ms: 1.27x faster                                                 |
| pycparser               | 916 ms                                                 | 721 ms: 1.27x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.4 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 534 ms: 1.25x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.91 us: 1.24x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.18 ms: 1.24x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.70 ms: 1.23x faster                                                 |
| async_generators        | 234 ms                                                 | 191 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                |
| fannkuch                | 317 ms                                                 | 262 ms: 1.21x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.37 ms: 1.21x faster                                                 |
| aiohttp                 | 1.27 ms                                                | 1.06 ms: 1.20x faster                                                 |
| gunicorn                | 1.35 ms                                                | 1.13 ms: 1.20x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.30 ms: 1.20x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 63.2 ms: 1.18x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.18x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 31.4 ms: 1.18x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.33 ms: 1.18x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.17 ms: 1.17x faster                                                 |
| generators              | 32.7 ms                                                | 27.9 ms: 1.17x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 31.9 ns: 1.17x faster                                                 |
| coroutines              | 20.2 ms                                                | 17.3 ms: 1.17x faster                                                 |
| sympy_str               | 169 ms                                                 | 147 ms: 1.15x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 476 us: 1.15x faster                                                  |
| scimark_fft             | 230 ms                                                 | 201 ms: 1.15x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 81.7 ms: 1.15x faster                                                 |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.15x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.29 us: 1.14x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| pylint                  | 307 ms                                                 | 271 ms: 1.13x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 47.9 ms: 1.13x faster                                                 |
| nqueens                 | 68.2 ms                                                | 60.6 ms: 1.13x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 64.4 ms: 1.12x faster                                                 |
| regex_effbot            | 2.46 ms                                                | 2.20 ms: 1.12x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| 2to3                    | 201 ms                                                 | 181 ms: 1.11x faster                                                  |
| json_dumps              | 8.40 ms                                                | 7.58 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.22 ms: 1.07x faster                                                 |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| bench_mp_pool           | 39.7 ms                                                | 37.1 ms: 1.07x faster                                                 |
| json                    | 3.08 ms                                                | 2.92 ms: 1.06x faster                                                 |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 75.2 ms: 1.04x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.62 us: 1.02x faster                                                 |
| pickle                  | 7.35 us                                                | 7.18 us: 1.02x faster                                                 |
| regex_dna               | 162 ms                                                 | 169 ms: 1.05x slower                                                  |
| pickle_dict             | 17.9 us                                                | 19.2 us: 1.07x slower                                                 |
| regex_v8                | 17.6 ms                                                | 20.5 ms: 1.17x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (4): unpickle, pickle_list, mdp, pidigits
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220405-3.11.0a7-2e49bd0/bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0.json: mypy
