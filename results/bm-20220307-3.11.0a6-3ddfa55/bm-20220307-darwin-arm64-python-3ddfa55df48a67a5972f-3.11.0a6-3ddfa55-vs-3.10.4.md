
# Results vs. 3.10.4

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: darwin-arm64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 165 ms: 1.22x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.60 ms: 1.26x faster                                                 |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                |
| html5lib       | 44.2 ms                                                | 33.4 ms: 1.33x faster                                                 |
| tornado_http   | 91.5 ms                                                | 72.8 ms: 1.26x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 66.5 ms: 1.40x faster                                                 |
| float          | 72.4 ms                                                | 52.8 ms: 1.37x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.2 ms: 1.27x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| regex_dna      | 162 ms                                                 | 162 ms: 1.00x slower                                                  |
| regex_v8       | 17.6 ms                                                | 17.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 204 us: 1.39x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 36.1 ms: 1.24x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 168 us: 1.21x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.65 ms: 1.10x faster                                                 |
| json_loads           | 16.9 us                                                | 16.0 us: 1.06x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 68.3 ms: 1.06x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.05x faster                                                  |
| pickle               | 7.35 us                                                | 7.15 us: 1.03x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.5 us: 1.03x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.63 us: 1.02x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                | 9.77 ms: 1.10x slower                                                 |
| python_startup         | 11.9 ms                                                | 15.6 ms: 1.31x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.66 ms: 1.37x faster                                                 |
| django_template | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.1 ms: 1.21x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 31.2 ms: 1.19x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.97 ms: 1.73x faster                                                 |
| logging_silent          | 119 ns                                                 | 74.5 ns: 1.60x faster                                                 |
| scimark_sor             | 126 ms                                                 | 80.0 ms: 1.58x faster                                                 |
| richards                | 51.4 ms                                                | 33.1 ms: 1.55x faster                                                 |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                                  |
| raytrace                | 325 ms                                                 | 214 ms: 1.52x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.08 us: 1.50x faster                                                 |
| logging_format          | 4.97 us                                                | 3.36 us: 1.48x faster                                                 |
| scimark_lu              | 109 ms                                                 | 74.4 ms: 1.47x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 711 ms: 1.43x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 344 ms: 1.42x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 51.3 ms: 1.41x faster                                                 |
| pyflate                 | 453 ms                                                 | 322 ms: 1.41x faster                                                  |
| nbody                   | 93.3 ms                                                | 66.5 ms: 1.40x faster                                                 |
| async_tree_none         | 400 ms                                                 | 288 ms: 1.39x faster                                                  |
| chaos                   | 66.7 ms                                                | 48.1 ms: 1.39x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 204 us: 1.39x faster                                                  |
| float                   | 72.4 ms                                                | 52.8 ms: 1.37x faster                                                 |
| mako                    | 10.5 ms                                                | 7.66 ms: 1.37x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 57.1 ms: 1.37x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.67 ms: 1.35x faster                                                 |
| html5lib                | 44.2 ms                                                | 33.4 ms: 1.33x faster                                                 |
| thrift                  | 580 us                                                 | 443 us: 1.31x faster                                                  |
| regex_compile           | 96.4 ms                                                | 76.2 ms: 1.27x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.60 ms: 1.26x faster                                                 |
| tornado_http            | 91.5 ms                                                | 72.8 ms: 1.26x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 27.4 us: 1.26x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 76.8 ms: 1.25x faster                                                 |
| pycparser               | 916 ms                                                 | 737 ms: 1.24x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 36.1 ms: 1.24x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 489 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 542 ms: 1.23x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 999 ms: 1.23x faster                                                  |
| django_template         | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                 |
| 2to3                    | 201 ms                                                 | 165 ms: 1.22x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.1 ms: 1.21x faster                                                 |
| deepcopy                | 281 us                                                 | 232 us: 1.21x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 168 us: 1.21x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 729 us: 1.21x faster                                                  |
| aiohttp                 | 1.27 ms                                                | 1.05 ms: 1.21x faster                                                 |
| fannkuch                | 317 ms                                                 | 265 ms: 1.20x faster                                                  |
| async_generators        | 234 ms                                                 | 195 ms: 1.20x faster                                                  |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                |
| dulwich_log             | 37.1 ms                                                | 31.1 ms: 1.19x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 31.2 ms: 1.19x faster                                                 |
| gunicorn                | 1.35 ms                                                | 1.14 ms: 1.19x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.01 us: 1.18x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.57 ms: 1.17x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.36 ms: 1.15x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.9 ms: 1.15x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 65.2 ms: 1.15x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.19 ms: 1.15x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.14x faster                                                 |
| scimark_fft             | 230 ms                                                 | 203 ms: 1.14x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.30 us: 1.13x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                 |
| generators              | 32.7 ms                                                | 29.2 ms: 1.12x faster                                                 |
| nqueens                 | 68.2 ms                                                | 61.1 ms: 1.12x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 176 ms: 1.12x faster                                                  |
| flaskblogging           | 2.75 ms                                                | 2.48 ms: 1.11x faster                                                 |
| sympy_str               | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| json                    | 3.08 ms                                                | 2.80 ms: 1.10x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 85.3 ms: 1.10x faster                                                 |
| json_dumps              | 8.40 ms                                                | 7.65 ms: 1.10x faster                                                 |
| sympy_expand            | 275 ms                                                 | 253 ms: 1.09x faster                                                  |
| pylint                  | 307 ms                                                 | 283 ms: 1.09x faster                                                  |
| pathlib                 | 28.8 ms                                                | 26.7 ms: 1.08x faster                                                 |
| coroutines              | 20.2 ms                                                | 18.7 ms: 1.08x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 513 us: 1.07x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.26 ms: 1.06x faster                                                 |
| json_loads              | 16.9 us                                                | 16.0 us: 1.06x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 68.3 ms: 1.06x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.58 sec: 1.05x faster                                                |
| xml_etree_parse         | 106 ms                                                 | 102 ms: 1.05x faster                                                  |
| dask                    | 265 ms                                                 | 255 ms: 1.04x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 75.2 ms: 1.04x faster                                                 |
| pickle                  | 7.35 us                                                | 7.15 us: 1.03x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 652 ms: 1.03x faster                                                  |
| pickle_dict             | 17.9 us                                                | 17.5 us: 1.03x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.63 us: 1.02x faster                                                 |
| telco                   | 3.63 ms                                                | 3.57 ms: 1.02x faster                                                 |
| regex_effbot            | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_dna               | 162 ms                                                 | 162 ms: 1.00x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                                 |
| regex_v8                | 17.6 ms                                                | 17.8 ms: 1.01x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.01x slower                                                 |
| comprehensions          | 17.6 us                                                | 18.2 us: 1.03x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 9.77 ms: 1.10x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 44.5 ms: 1.12x slower                                                 |
| coverage                | 42.0 ms                                                | 50.9 ms: 1.21x slower                                                 |
| python_startup          | 11.9 ms                                                | 15.6 ms: 1.31x slower                                                 |
| unpack_sequence         | 37.4 ns                                                | 90.8 ns: 2.43x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: mypy2
