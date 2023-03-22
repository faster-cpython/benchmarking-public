
# Results vs. 3.10.4

- fork: python
- ref: a0ad63e70e3682cdf7e8
- machine: darwin-arm64
- commit hash: a0ad63e
- commit date: 2022-09-04
- overall geometric mean: 1.22x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.59 ms: 1.26x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| html5lib       | 44.2 ms                                                | 36.4 ms: 1.21x faster                                                 |
| tornado_http   | 91.5 ms                                                | 70.1 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                 |
| float          | 72.4 ms                                                | 51.3 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.3 ms: 1.28x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.4 ms: 1.07x faster                                                 |
| regex_dna      | 162 ms                                                 | 151 ms: 1.07x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.72 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 198 us: 1.43x faster                                                  |
| json_dumps           | 8.40 ms                                                | 6.10 ms: 1.38x faster                                                 |
| xml_etree_process    | 44.8 ms                                                | 34.5 ms: 1.30x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 160 us: 1.27x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 47.2 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 64.5 ms: 1.12x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 95.9 ms: 1.11x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.58 us: 1.04x faster                                                 |
| unpickle             | 9.89 us                                                | 9.64 us: 1.03x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.02x slower                                                 |
| pickle               | 7.35 us                                                | 7.59 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.07 ms: 1.31x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.16 ms: 1.24x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.97 ms: 1.32x faster                                                 |
| django_template | 27.3 ms                                                | 20.9 ms: 1.30x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 29.9 ms: 1.24x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.1 ms: 1.22x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 64.5 ns: 1.85x faster                                                 |
| deltablue               | 5.14 ms                                                | 2.84 ms: 1.81x faster                                                 |
| raytrace                | 325 ms                                                 | 211 ms: 1.54x faster                                                  |
| richards                | 51.4 ms                                                | 33.4 ms: 1.54x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 51.1 ms: 1.53x faster                                                 |
| scimark_lu              | 109 ms                                                 | 72.7 ms: 1.50x faster                                                 |
| nbody                   | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 198 us: 1.43x faster                                                  |
| go                      | 165 ms                                                 | 117 ms: 1.41x faster                                                  |
| float                   | 72.4 ms                                                | 51.3 ms: 1.41x faster                                                 |
| async_tree_none         | 400 ms                                                 | 284 ms: 1.41x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 734 ms: 1.39x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 24.8 us: 1.39x faster                                                 |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                                 |
| json_dumps              | 8.40 ms                                                | 6.10 ms: 1.38x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.00 ms: 1.36x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.16 ms: 1.35x faster                                                 |
| chaos                   | 66.7 ms                                                | 49.5 ms: 1.35x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 53.8 ms: 1.35x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 71.7 ms: 1.34x faster                                                 |
| thrift                  | 580 us                                                 | 441 us: 1.32x faster                                                  |
| mako                    | 10.5 ms                                                | 7.97 ms: 1.32x faster                                                 |
| pyflate                 | 453 ms                                                 | 345 ms: 1.31x faster                                                  |
| python_startup          | 11.9 ms                                                | 9.07 ms: 1.31x faster                                                 |
| deepcopy                | 281 us                                                 | 215 us: 1.31x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.1 ms: 1.31x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.84 ms: 1.30x faster                                                 |
| django_template         | 27.3 ms                                                | 20.9 ms: 1.30x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 949 ms: 1.30x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 34.5 ms: 1.30x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 468 ms: 1.30x faster                                                  |
| pycparser               | 916 ms                                                 | 711 ms: 1.29x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 381 ms: 1.29x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.85 us: 1.28x faster                                                 |
| regex_compile           | 96.4 ms                                                | 75.3 ms: 1.28x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.63 us: 1.28x faster                                                 |
| scimark_sor             | 126 ms                                                 | 99.0 ms: 1.27x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 160 us: 1.27x faster                                                  |
| logging_format          | 4.97 us                                                | 3.92 us: 1.27x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.59 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 530 ms: 1.26x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.12 ms: 1.25x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 29.9 ms: 1.24x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.16 ms: 1.24x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.22 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.80 ms: 1.24x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 61.5 ms: 1.22x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 449 us: 1.22x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.1 ms: 1.22x faster                                                 |
| html5lib                | 44.2 ms                                                | 36.4 ms: 1.21x faster                                                 |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 31.7 ms: 1.20x faster                                                 |
| fannkuch                | 317 ms                                                 | 268 ms: 1.18x faster                                                  |
| async_generators        | 234 ms                                                 | 199 ms: 1.18x faster                                                  |
| scimark_fft             | 230 ms                                                 | 197 ms: 1.17x faster                                                  |
| pylint                  | 307 ms                                                 | 264 ms: 1.16x faster                                                  |
| nqueens                 | 68.2 ms                                                | 58.7 ms: 1.16x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.16x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 47.2 ms: 1.15x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 33.0 ns: 1.13x faster                                                 |
| generators              | 32.7 ms                                                | 29.1 ms: 1.12x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 64.5 ms: 1.12x faster                                                 |
| sympy_expand            | 275 ms                                                 | 247 ms: 1.12x faster                                                  |
| sympy_str               | 169 ms                                                 | 152 ms: 1.12x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 84.0 ms: 1.11x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 95.9 ms: 1.11x faster                                                 |
| json                    | 3.08 ms                                                | 2.82 ms: 1.09x faster                                                 |
| 2to3                    | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| telco                   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.55 sec: 1.07x faster                                                |
| regex_v8                | 17.6 ms                                                | 16.4 ms: 1.07x faster                                                 |
| regex_dna               | 162 ms                                                 | 151 ms: 1.07x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.06x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| coroutines              | 20.2 ms                                                | 19.3 ms: 1.04x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.58 us: 1.04x faster                                                 |
| unpickle                | 9.89 us                                                | 9.64 us: 1.03x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 77.0 ms: 1.01x faster                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.02x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 40.9 ms: 1.03x slower                                                 |
| pickle                  | 7.35 us                                                | 7.59 us: 1.03x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.72 ms: 1.11x slower                                                 |
| coverage                | 42.0 ms                                                | 54.3 ms: 1.29x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220904-3.12.0a0-a0ad63e/bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e.json: mypy
