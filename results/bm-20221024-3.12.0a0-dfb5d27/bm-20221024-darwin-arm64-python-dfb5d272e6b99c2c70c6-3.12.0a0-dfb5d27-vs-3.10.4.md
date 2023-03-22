
# Results vs. 3.10.4

- fork: python
- ref: dfb5d272e6b99c2c70c6
- machine: darwin-arm64
- commit hash: dfb5d27
- commit date: 2022-10-24
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.61 ms: 1.26x faster                                                 |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| html5lib       | 44.2 ms                                                | 36.5 ms: 1.21x faster                                                 |
| tornado_http   | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.6 ms: 1.45x faster                                                 |
| float          | 72.4 ms                                                | 56.2 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.1 ms: 1.27x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.4 ms: 1.07x faster                                                 |
| regex_dna      | 162 ms                                                 | 152 ms: 1.06x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.74 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.13 ms: 1.37x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 208 us: 1.36x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.25x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 91.0 ms: 1.17x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 47.3 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 64.9 ms: 1.11x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.53 us: 1.06x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| unpickle             | 9.89 us                                                | 9.77 us: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.54 us: 1.03x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.88 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.19 ms: 1.30x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.21 ms: 1.23x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.13 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.7 ms: 1.25x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.2 ms: 1.23x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.74 ms: 1.88x faster                                                 |
| logging_silent          | 119 ns                                                 | 65.8 ns: 1.81x faster                                                 |
| richards                | 51.4 ms                                                | 33.5 ms: 1.53x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 51.3 ms: 1.52x faster                                                 |
| scimark_lu              | 109 ms                                                 | 71.9 ms: 1.52x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 325 ms: 1.51x faster                                                  |
| nbody                   | 93.3 ms                                                | 64.6 ms: 1.45x faster                                                 |
| raytrace                | 325 ms                                                 | 227 ms: 1.43x faster                                                  |
| async_tree_none         | 400 ms                                                 | 287 ms: 1.40x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.7 ms: 1.39x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.39x faster                                                  |
| go                      | 165 ms                                                 | 119 ms: 1.38x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.13 ms: 1.37x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.00 ms: 1.36x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 208 us: 1.36x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.17 ms: 1.35x faster                                                 |
| chaos                   | 66.7 ms                                                | 50.3 ms: 1.33x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 72.6 ms: 1.32x faster                                                 |
| thrift                  | 580 us                                                 | 441 us: 1.32x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 55.4 ms: 1.31x faster                                                 |
| pycparser               | 916 ms                                                 | 703 ms: 1.30x faster                                                  |
| python_startup          | 11.9 ms                                                | 9.19 ms: 1.30x faster                                                 |
| mako                    | 10.5 ms                                                | 8.13 ms: 1.29x faster                                                 |
| float                   | 72.4 ms                                                | 56.2 ms: 1.29x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.92 ms: 1.29x faster                                                 |
| tornado_http            | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| pyflate                 | 453 ms                                                 | 355 ms: 1.28x faster                                                  |
| regex_compile           | 96.4 ms                                                | 76.1 ms: 1.27x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.66 us: 1.26x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.4 ms: 1.26x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.61 ms: 1.26x faster                                                 |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.25x faster                                                 |
| logging_format          | 4.97 us                                                | 3.97 us: 1.25x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.25x faster                                                  |
| scimark_sor             | 126 ms                                                 | 101 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.77 ms: 1.25x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 488 ms: 1.24x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 996 ms: 1.24x faster                                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.21 ms: 1.23x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 30.2 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 544 ms: 1.23x faster                                                  |
| html5lib                | 44.2 ms                                                | 36.5 ms: 1.21x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 452 us: 1.21x faster                                                  |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| genshi_text             | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.20x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 29.0 us: 1.18x faster                                                 |
| fannkuch                | 317 ms                                                 | 268 ms: 1.18x faster                                                  |
| async_generators        | 234 ms                                                 | 199 ms: 1.18x faster                                                  |
| scimark_fft             | 230 ms                                                 | 196 ms: 1.18x faster                                                  |
| deepcopy                | 281 us                                                 | 239 us: 1.17x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 91.0 ms: 1.17x faster                                                 |
| pylint                  | 307 ms                                                 | 264 ms: 1.17x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.05 us: 1.16x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 47.3 ms: 1.15x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.6 ms: 1.14x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 173 ms: 1.13x faster                                                  |
| nqueens                 | 68.2 ms                                                | 60.3 ms: 1.13x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 33.2 ns: 1.13x faster                                                 |
| generators              | 32.7 ms                                                | 29.3 ms: 1.12x faster                                                 |
| sympy_expand            | 275 ms                                                 | 247 ms: 1.12x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 64.9 ms: 1.11x faster                                                 |
| sympy_str               | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.52 sec: 1.09x faster                                                |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 86.1 ms: 1.09x faster                                                 |
| 2to3                    | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| telco                   | 3.63 ms                                                | 3.37 ms: 1.08x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.4 ms: 1.07x faster                                                 |
| coroutines              | 20.2 ms                                                | 18.9 ms: 1.06x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.53 us: 1.06x faster                                                 |
| regex_dna               | 162 ms                                                 | 152 ms: 1.06x faster                                                  |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 76.8 ms: 1.02x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.45 us: 1.02x faster                                                 |
| unpickle                | 9.89 us                                                | 9.77 us: 1.01x faster                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.54 us: 1.03x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.88 us: 1.03x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 41.7 ms: 1.05x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.74 ms: 1.11x slower                                                 |
| coverage                | 42.0 ms                                                | 53.1 ms: 1.26x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.12.0a0-dfb5d27/bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27.json: mypy
