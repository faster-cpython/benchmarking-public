
# Results vs. 3.10.4

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: darwin-arm64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.22x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.75 ms: 1.22x faster                                                 |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                |
| html5lib       | 44.2 ms                                                | 33.2 ms: 1.33x faster                                                 |
| tornado_http   | 91.5 ms                                                | 70.4 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                 |
| float          | 72.4 ms                                                | 51.4 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 78.4 ms: 1.23x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                 |
| regex_dna      | 162 ms                                                 | 140 ms: 1.15x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 212 us: 1.34x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.9 ms: 1.25x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 181 us: 1.12x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 49.0 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 65.5 ms: 1.10x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.77 ms: 1.08x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.1 us: 1.05x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.71 us: 1.03x faster                                                 |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.61 us: 1.03x faster                                                 |
| pickle               | 7.35 us                                                | 7.17 us: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.22 ms: 1.29x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.24 ms: 1.23x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.5 ms: 1.27x faster                                                 |
| mako            | 10.5 ms                                                | 8.40 ms: 1.25x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 31.6 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.22x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.74 ms: 1.88x faster                                                 |
| logging_silent          | 119 ns                                                 | 67.5 ns: 1.77x faster                                                 |
| scimark_sor             | 126 ms                                                 | 79.2 ms: 1.59x faster                                                 |
| raytrace                | 325 ms                                                 | 207 ms: 1.58x faster                                                  |
| richards                | 51.4 ms                                                | 33.8 ms: 1.52x faster                                                 |
| go                      | 165 ms                                                 | 110 ms: 1.50x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 52.1 ms: 1.50x faster                                                 |
| scimark_lu              | 109 ms                                                 | 73.7 ms: 1.48x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 48.9 ms: 1.48x faster                                                 |
| nbody                   | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 705 ms: 1.45x faster                                                  |
| float                   | 72.4 ms                                                | 51.4 ms: 1.41x faster                                                 |
| pyflate                 | 453 ms                                                 | 322 ms: 1.41x faster                                                  |
| async_tree_none         | 400 ms                                                 | 286 ms: 1.40x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.7 ms: 1.39x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 356 ms: 1.38x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 71.7 ms: 1.34x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 212 us: 1.34x faster                                                  |
| html5lib                | 44.2 ms                                                | 33.2 ms: 1.33x faster                                                 |
| chaos                   | 66.7 ms                                                | 50.6 ms: 1.32x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 26.2 us: 1.31x faster                                                 |
| thrift                  | 580 us                                                 | 443 us: 1.31x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.4 ms: 1.30x faster                                                 |
| pycparser               | 916 ms                                                 | 709 ms: 1.29x faster                                                  |
| python_startup          | 11.9 ms                                                | 9.22 ms: 1.29x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 470 ms: 1.29x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.60 us: 1.29x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.92 ms: 1.28x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 966 ms: 1.28x faster                                                  |
| logging_format          | 4.97 us                                                | 3.90 us: 1.27x faster                                                 |
| django_template         | 27.3 ms                                                | 21.5 ms: 1.27x faster                                                 |
| deepcopy                | 281 us                                                 | 222 us: 1.27x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 534 ms: 1.25x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.90 us: 1.25x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 35.9 ms: 1.25x faster                                                 |
| mako                    | 10.5 ms                                                | 8.40 ms: 1.25x faster                                                 |
| regex_compile           | 96.4 ms                                                | 78.4 ms: 1.23x faster                                                 |
| aiohttp                 | 1.27 ms                                                | 1.03 ms: 1.23x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.24 ms: 1.23x faster                                                 |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                |
| chameleon               | 5.79 ms                                                | 4.75 ms: 1.22x faster                                                 |
| fannkuch                | 317 ms                                                 | 261 ms: 1.21x faster                                                  |
| regex_effbot            | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.29 ms: 1.20x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.44 ms: 1.19x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.8 ms: 1.19x faster                                                 |
| gunicorn                | 1.35 ms                                                | 1.14 ms: 1.19x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 31.6 ms: 1.18x faster                                                 |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.3 ns: 1.16x faster                                                 |
| regex_dna               | 162 ms                                                 | 140 ms: 1.15x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 33.0 ms: 1.15x faster                                                 |
| scimark_fft             | 230 ms                                                 | 201 ms: 1.15x faster                                                  |
| pylint                  | 307 ms                                                 | 268 ms: 1.14x faster                                                  |
| generators              | 32.7 ms                                                | 28.6 ms: 1.14x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.38 ms: 1.14x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 482 us: 1.13x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.13x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.21 ms: 1.13x faster                                                 |
| nqueens                 | 68.2 ms                                                | 60.4 ms: 1.13x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 181 us: 1.12x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 83.6 ms: 1.12x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.32 us: 1.12x faster                                                 |
| regex_v8                | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                 |
| sympy_str               | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| sympy_expand            | 275 ms                                                 | 249 ms: 1.11x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 49.0 ms: 1.10x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 65.5 ms: 1.10x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 179 ms: 1.10x faster                                                  |
| 2to3                    | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| json_dumps              | 8.40 ms                                                | 7.77 ms: 1.08x faster                                                 |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.23 ms: 1.07x faster                                                 |
| telco                   | 3.63 ms                                                | 3.41 ms: 1.07x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.56 sec: 1.06x faster                                                |
| json                    | 3.08 ms                                                | 2.92 ms: 1.06x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.1 us: 1.05x faster                                                 |
| pickle_list             | 2.80 us                                                | 2.71 us: 1.03x faster                                                 |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.61 us: 1.03x faster                                                 |
| pickle                  | 7.35 us                                                | 7.17 us: 1.02x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 76.8 ms: 1.02x faster                                                 |
| bench_mp_pool           | 39.7 ms                                                | 41.2 ms: 1.04x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (2): pidigits, unpickle
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220506-3.11.0b1-8d32a5c/bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c.json: mypy
