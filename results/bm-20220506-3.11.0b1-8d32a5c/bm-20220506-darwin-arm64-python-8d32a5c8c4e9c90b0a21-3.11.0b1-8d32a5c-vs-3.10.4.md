
# Results vs. 3.10.4

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: darwin-arm64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.64 ms: 1.25x faster                                                 |
| docutils       | 1.78 sec                                               | 1.44 sec: 1.23x faster                                                |
| html5lib       | 44.2 ms                                                | 33.8 ms: 1.31x faster                                                 |
| tornado_http   | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                 |
| float          | 72.4 ms                                                | 54.1 ms: 1.34x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.9 ms: 1.24x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.06 ms: 1.19x faster                                                 |
| regex_v8       | 17.6 ms                                                | 15.1 ms: 1.16x faster                                                 |
| regex_dna      | 162 ms                                                 | 142 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 219 us: 1.29x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.5 ms: 1.26x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 179 us: 1.14x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.6 ms: 1.11x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.69 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 69.0 ms: 1.05x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| pickle               | 7.35 us                                                | 7.16 us: 1.03x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.74 us: 1.02x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.63 us: 1.02x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 106 ms: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 9.86 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.7 ms: 1.25x faster                                                 |
| mako            | 10.5 ms                                                | 8.45 ms: 1.24x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.6 ms: 1.21x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.4 ms: 1.19x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.69 ms: 1.91x faster                                                 |
| logging_silent          | 119 ns                                                 | 70.7 ns: 1.69x faster                                                 |
| scimark_sor             | 126 ms                                                 | 76.6 ms: 1.65x faster                                                 |
| raytrace                | 325 ms                                                 | 205 ms: 1.59x faster                                                  |
| go                      | 165 ms                                                 | 106 ms: 1.56x faster                                                  |
| scimark_lu              | 109 ms                                                 | 72.2 ms: 1.51x faster                                                 |
| richards                | 51.4 ms                                                | 34.3 ms: 1.50x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 52.3 ms: 1.49x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 49.3 ms: 1.47x faster                                                 |
| nbody                   | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 710 ms: 1.44x faster                                                  |
| pyflate                 | 453 ms                                                 | 320 ms: 1.41x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 357 ms: 1.38x faster                                                  |
| async_tree_none         | 400 ms                                                 | 292 ms: 1.37x faster                                                  |
| float                   | 72.4 ms                                                | 54.1 ms: 1.34x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 71.7 ms: 1.34x faster                                                 |
| chaos                   | 66.7 ms                                                | 50.1 ms: 1.33x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.51 us: 1.32x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.82 ms: 1.31x faster                                                 |
| thrift                  | 580 us                                                 | 443 us: 1.31x faster                                                  |
| html5lib                | 44.2 ms                                                | 33.8 ms: 1.31x faster                                                 |
| logging_format          | 4.97 us                                                | 3.80 us: 1.31x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 219 us: 1.29x faster                                                  |
| pycparser               | 916 ms                                                 | 710 ms: 1.29x faster                                                  |
| tornado_http            | 91.5 ms                                                | 71.3 ms: 1.28x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 35.5 ms: 1.26x faster                                                 |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.25x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.64 ms: 1.25x faster                                                 |
| mako                    | 10.5 ms                                                | 8.45 ms: 1.24x faster                                                 |
| 2to3                    | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| regex_compile           | 96.4 ms                                                | 77.9 ms: 1.24x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 542 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.44 sec: 1.23x faster                                                |
| mypy2                   | 307 ms                                                 | 251 ms: 1.22x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 723 us: 1.22x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 30.5 ms: 1.22x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 30.6 ms: 1.21x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 499 ms: 1.21x faster                                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.38 ms: 1.20x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.5 ms: 1.20x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.03 sec: 1.20x faster                                                |
| fannkuch                | 317 ms                                                 | 265 ms: 1.20x faster                                                  |
| aiohttp                 | 1.27 ms                                                | 1.06 ms: 1.20x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.4 ms: 1.19x faster                                                 |
| regex_effbot            | 2.46 ms                                                | 2.06 ms: 1.19x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 29.1 us: 1.18x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.4 ms: 1.17x faster                                                 |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                                  |
| gunicorn                | 1.35 ms                                                | 1.15 ms: 1.17x faster                                                 |
| generators              | 32.7 ms                                                | 28.1 ms: 1.17x faster                                                 |
| regex_v8                | 17.6 ms                                                | 15.1 ms: 1.16x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 32.4 ns: 1.15x faster                                                 |
| deepcopy                | 281 us                                                 | 244 us: 1.15x faster                                                  |
| scimark_fft             | 230 ms                                                 | 201 ms: 1.15x faster                                                  |
| dask                    | 265 ms                                                 | 232 ms: 1.15x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.38 ms: 1.14x faster                                                 |
| regex_dna               | 162 ms                                                 | 142 ms: 1.14x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 179 us: 1.14x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 11.8 ms: 1.13x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.21 ms: 1.13x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.11 us: 1.13x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.44 ms: 1.13x faster                                                 |
| pylint                  | 307 ms                                                 | 275 ms: 1.12x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.0 ms: 1.12x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 176 ms: 1.12x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 48.6 ms: 1.11x faster                                                 |
| nqueens                 | 68.2 ms                                                | 61.3 ms: 1.11x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 84.6 ms: 1.11x faster                                                 |
| sympy_expand            | 275 ms                                                 | 250 ms: 1.10x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.34 us: 1.10x faster                                                 |
| sympy_str               | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 499 us: 1.10x faster                                                  |
| json_dumps              | 8.40 ms                                                | 7.69 ms: 1.09x faster                                                 |
| json                    | 3.08 ms                                                | 2.85 ms: 1.08x faster                                                 |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.56 sec: 1.07x faster                                                |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.24 ms: 1.07x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.1 ms: 1.06x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 69.0 ms: 1.05x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 651 ms: 1.03x faster                                                  |
| pickle                  | 7.35 us                                                | 7.16 us: 1.03x faster                                                 |
| pickle_list             | 2.80 us                                                | 2.74 us: 1.02x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.63 us: 1.02x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 76.6 ms: 1.02x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 106 ms: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                 |
| comprehensions          | 17.6 us                                                | 19.2 us: 1.09x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 43.5 ms: 1.10x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 9.86 ms: 1.11x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: coverage
